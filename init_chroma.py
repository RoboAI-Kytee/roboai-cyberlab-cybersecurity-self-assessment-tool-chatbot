import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

from list_all_documents import list_pdfs_in_folder

import yaml

config = yaml.safe_load(open("config.yml"))

def create_chroma_local_db():
    # Verify files exist and handle invalid files
    valid_files = []
    for path in list_pdfs_in_folder(): 
        if os.path.exists(path) and path.endswith('.pdf'):
            valid_files.append(path)
        else:
            print(f"Skipping invalid or non-existent file: {path}")
    
    # Load PDFs using PyPDFLoader
    data = []
    for path in valid_files:
        loader = PyPDFLoader(file_path=path)
        try:
            data.extend(loader.load())
        except Exception as e:
            print(f"Error loading PDF at {path}: {e}")
    
    # Check if data was loaded successfully
    if not data:
        raise ValueError("No valid documents were loaded. Check the input files.")
    
    # Load and split PDF content
    text_splitter = RecursiveCharacterTextSplitter(chunk_size= config['chunk_size'], chunk_overlap= config['chunk_overlap'])
    chunks = text_splitter.split_documents(data)
    
    # Store the document embeddings in Chroma
    vector_db = Chroma.from_documents(
        documents= chunks,
        embedding= OpenAIEmbeddings(model=config['openAIEmbeddings_model']),
        persist_directory= config['chromadb_folder'],
        collection_name= config['chroma_collection_name'] 
    )
    
    print("Vector database created successfully.")

    return vector_db

def init_local_vector_db():
    persist_directory= config['chromadb_folder']
    # Check if ChromaDB already exists
    if os.path.exists(persist_directory):
        print("Existing ChromaDB found. Loading existing database...")
        vector_db = Chroma(
            persist_directory=persist_directory,
            embedding_function=OpenAIEmbeddings(model=config['openAIEmbeddings_model']),
            collection_name=config['chroma_collection_name']
        )
        return vector_db

    # If no existing database, create a new one
    print("No existing ChromaDB found. Creating new database...")
    return create_chroma_local_db()

if __name__ == "__main__":
    init_local_vector_db()