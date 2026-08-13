from langchain_text_splitters import RecursiveCharacterTextSplitter


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)


def chunk(parsed_content):
    """
    Takes parsed content from parser.py and returns chunked content with metadata.
    """

    content = parsed_content["content"]
    metadata = parsed_content["metadata"]

    text = "\n\n".join(content)

    chunks = text_splitter.split_text(text)

    chunked_data = []

    for chunk_id, chunk_text in enumerate(chunks):
        chunked_data.append({
            "chunk_id": chunk_id,
            "text": chunk_text,
            "metadata": {
                "filename": metadata["file_name"],
                "file_size": metadata["file_size"],
                "format": metadata["file_type"]
            }
        })

    return chunked_data