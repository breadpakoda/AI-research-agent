import fitz


def parse(file_path:str)->str:
    """
    Extracts the pdf file's text while preserving the file structure
    """

    try:
        pdf=fitz.open(file_path)
        text=""

        for page in pdf:
            text+=page.get_text("text")+"\n"
        pdf.close()

        return text.strip()

    except Exception as e:
        raise Exception(f"Failed to read the file: {e}")