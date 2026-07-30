import fitz


def parse(file_path: str) -> str:
    """
    Extract text from a PDF while preserving page order.
    """
    try:
        pages = []

        with fitz.open(file_path) as pdf:
            for page in pdf:
                pages.append(page.get_text("text"))

        return "\n".join(pages)

    except Exception as e:
        raise RuntimeError(f"Failed to read PDF: {e}")