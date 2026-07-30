from pathlib import Path



def extension_checker(file_name):
    supported_path={".txt",".pdf",".docx"}
    if Path(file_name).suffix.lower not in supported_path:
        raise ValueError(f"Unsupported file type {Path(file_name).suffix}")

    elif Path(file_name).suffix.lower()==".txt":


    elif Path(file_name).suffix.lower()==".pdf":


    elif Path(file_name).suffix.lower()==".docx":
