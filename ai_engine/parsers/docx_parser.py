from docx import Document


def parse(file_path: str) -> str:
    try:
        doc = Document(file_path)

        paragraphs = []

        for paragraph in doc.paragraphs:
            paragraphs.append(paragraph.text)

        return paragraphs

    except Exception as e:
        raise Exception(f"Failed to parse DOCX: {e}")


