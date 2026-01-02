import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# Directory where PDFs are stored
PDF_DIR = "data/pdfs"
# Directory where Chroma vector DB will be persisted
DB_DIR = "chroma_db"


def ingest_pdfs():
    documents = []

    # Load all PDFs
    for filename in os.listdir(PDF_DIR):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(PDF_DIR, filename)
            # Load PDF using PyPDFLoader
            loader = PyPDFLoader(pdf_path)
            # Append loaded documents to the list
            documents.extend(loader.load())

    # Check if no documents were loaded
    if not documents:
        print("No PDF files found in data/pdfs/")
        return

    # Split documents into chunks for better embedding 
    # 1 chunk becomes one vector in Vector DB (Chunk = smallest retrievableunit of meaning)
    # 1000 is about 1-2 paragraphs aka a single idea
    # Overlap of 200 ensures context is maintained between chunks + retrieval quality improves
    # meaning often spans boundaries of chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    # Split documents into smaller chunks
    chunks = text_splitter.split_documents(documents)

    # Initialize embedding model (same as app.py)
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    # Create / overwrite Chroma vector database
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR
    )

    print(f"Successfully ingested {len(chunks)} chunks into ChromaDB")


if __name__ == "__main__":
    ingest_pdfs()
