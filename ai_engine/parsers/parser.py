from pathlib import Path
import pdf_parser
import docx_parser
import txt_parser



def extension_checker(file_name):
    supported_path={".txt",".pdf",".docx"}
    if Path(file_name).suffix.lower not in supported_path:
        raise ValueError(f"Unsupported file type {Path(file_name).suffix}")

    elif Path(file_name).suffix.lower()==".pdf":
        return pdf_parser.parse(file_name)


    elif Path(file_name).suffix.lower()==".txt":
        return txt_parser.parse(file_name)

    elif Path(file_name).suffix.lower()==".docx":
        return docx_parser.parse(file_name)