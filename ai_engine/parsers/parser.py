import os
from pathlib import Path

import pdf_parser
import docx_parser
import txt_parser


SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".docx"}


def parse(file_name):
    extension = Path(file_name).suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {extension}")

    if extension == ".pdf":
        content = pdf_parser.parse(file_name)
    elif extension == ".txt":
        content = txt_parser.parse(file_name)
    elif extension == ".docx":
        content = docx_parser.parse(file_name)
    else:
        raise ValueError(f"Unsupported file type: {extension}")

    metadata = {
        "file_name": os.path.basename(file_name),
        "file_size": os.path.getsize(file_name),
        "file_type": extension,
    }

    return {"content": content, "metadata": metadata}


# print(parse("parsers/langchain.docx"))


