import os
import uuid
from parsers import parser
from chunker import chunker
from embeddings import embedder
from vector_db import chroma_db

def ingest(file_path):
    """
    Orchestrates the complete document ingestion pipeline.
    It handles parsing, chunking, embedding, and storing in ChromaDB.
    """
    # 1. Parse the document
    parsed_document = parser.parse(file_path)

    # 2. Generate a unique document_id
    document_id = str(uuid.uuid4())

    # 3. Chunk the document
    chunks = chunker.chunk(parsed_document)

    # 4. Add the document_id to each chunk
    for chunk in chunks:
        chunk["document_id"] = document_id
        # Also include it in the metadata explicitly
        chunk["metadata"]["document_id"] = document_id

    # 5. Embed the chunks
    embedded_chunks = embedder.embed(chunks)

    # 6. Store the embedded chunks in ChromaDB
    chroma_db.add(embedded_chunks)

    # 7. Return a useful result summary
    return {
        "document_id": document_id,
        "filename": os.path.basename(file_path),
        "chunks": len(embedded_chunks),
        "status": "success"
    }
