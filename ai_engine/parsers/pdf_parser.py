import re

import fitz


def parse(file_path: str) -> str:
    try:
        paragraphs = []

        with fitz.open(file_path) as pdf:
            for page in pdf:
                page_text = page.get_text("text")
                page_paragraphs = re.split(r"\n\s*\n+", page_text)

                for paragraph in page_paragraphs:
                    cleaned = " ".join(paragraph.split())
                    if cleaned:
                        paragraphs.append(cleaned)

        return paragraphs

    except Exception as e:
        raise Exception(f"Failed to parse PDF: {e}")


# print(parse("parsers/Agentic AI Roadmap.pdf"))