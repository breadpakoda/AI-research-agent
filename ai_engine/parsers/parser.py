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
        return pdf_parser.parse(file_name)

    if extension == ".txt":
        return txt_parser.parse(file_name)

    if extension == ".docx":
        return docx_parser.parse(file_name)


# print(parse(input("Enter the file name: ")))