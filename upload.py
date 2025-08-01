from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore

embeddings = OllamaEmbeddings(model="llama3.2:3b")

file_path = "D:/RAG/bitcoin (1).pdf"
loader = PyPDFLoader(file_path)
data=loader.load_and_split()

url=""
api_key=""

qdrant = QdrantVectorStore.from_documents(
    data,
    embeddings,
    url=url,
    prefer_grpc=True,
    api_key=api_key,
    collection_name="bitcoin",
)
