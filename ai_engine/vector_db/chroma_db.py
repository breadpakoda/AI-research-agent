import chromadb
import os

_client = None
_collection = None

def initialize(persist_directory="./chroma_data"):
    """
    Create/connect to a persistent Chroma database.
    """
    global _client
    if _client is None:
        _client = chromadb.PersistentClient(path=persist_directory)
    get_collection()

def get_collection(collection_name="research_documents"):
    """
    Create or get the existing collection for research documents.
    """
    global _collection, _client
    if _client is None:
        initialize()
    if _collection is None:
        _collection = _client.get_or_create_collection(name=collection_name)
    return _collection

def add(chunks):
    """
    Add a list of chunk dictionaries to ChromaDB.
    Expected format for each chunk:
    {
        "document_id": "doc123",
        "chunk_id": 0,
        "text": "...",
        "embedding": [...],
        "metadata": {...}
    }
    """
    collection = get_collection()
    if not chunks:
        return

    ids = []
    documents = []
    embeddings = []
    metadatas = []

    for chunk in chunks:
        # Determine document ID (from chunk directly or its metadata)
        doc_id = chunk.get("document_id", chunk.get("metadata", {}).get("document_id", "unknown_doc"))
        
        # Handle chunk ID to ensure it is unique across documents
        raw_chunk_id = chunk.get("chunk_id", 0)
        
        # If it's already formatted as a string like "uuid_chunk_0", use it. Otherwise, format it.
        if isinstance(raw_chunk_id, str) and "_chunk_" in raw_chunk_id:
            unique_id = raw_chunk_id
        else:
            unique_id = f"{doc_id}_chunk_{raw_chunk_id}"
            
        ids.append(unique_id)
        documents.append(chunk["text"])
        embeddings.append(chunk["embedding"])
        
        # Prepare metadata and ensure document_id is present for easy deletion later
        meta = chunk.get("metadata", {}).copy()
        if "document_id" not in meta:
            meta["document_id"] = doc_id
        metadatas.append(meta)

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas
    )

def search(query_embedding, k=5):
    """
    Search for the top k most similar chunks given a query embedding.
    """
    collection = get_collection()
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )
    
    formatted_results = []
    
    # Chroma returns lists of lists (since you can query multiple embeddings at once)
    if not results["documents"] or not results["documents"][0]:
        return formatted_results
        
    # We only passed one query_embedding, so we take the first list of results
    docs = results["documents"][0]
    metas = results["metadatas"][0] if results["metadatas"] else [{}] * len(docs)
    dists = results["distances"][0] if results["distances"] else [0.0] * len(docs)
    
    for doc, meta, dist in zip(docs, metas, dists):
        formatted_results.append({
            "text": doc,
            "metadata": meta,
            "distance": dist
        })
        
    return formatted_results

def delete(document_id):
    """
    Delete all chunks belonging to a specific document.
    """
    collection = get_collection()
    
    # Delete all chunks where the metadata document_id matches
    collection.delete(
        where={"document_id": document_id}
    )
