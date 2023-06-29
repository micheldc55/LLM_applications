import os

from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from src.summarizers import build_openai_summarizer_chain


file_path = "/workspace/data/Price Optimization for Revenue Maximization at Scale.pdf"

# api_key = os.environ.get('OPENAI_API_KEY')

# summarizer = build_openai_summarizer_chain(api_key=api_key)

pdf_loader = PyPDFLoader(file_path=file_path)

pdf_loader.load_and_split(chunk_size=1000, )