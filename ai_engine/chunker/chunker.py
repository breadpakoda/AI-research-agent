from langchain_text_splitters import RecursiveCharacterTextSplitter
from parsers.parser import parse

text_splitter=RecursiveCharacterTextSplitter(chunk_size=200,overlap=20)

def splitter(file_name):
    return text_splitter()
