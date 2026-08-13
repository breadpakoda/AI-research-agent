from langchain_huggingface import HuggingFaceEmbeddings


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def embed(chunks):
    embeddings = embedding_model.embed_documents(
        [chunk["text"] for chunk in chunks]
    )

    for chunk, embedding in zip(chunks, embeddings):
        chunk["embedding"] = embedding

    return chunks