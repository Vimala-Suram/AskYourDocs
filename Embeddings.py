from langchain.embeddings import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

# Initializing embedding model for creating embeddings
embeddingModelName = HuggingFaceEmbeddings(model_name = "BAAI/bge-small-en-v1.5")

#Initializing qdrant client
client = QdrantClient(host = "local", port =6333, prefer_grpc = False)

def CreateEmbeddings(text, docID = "doc1"):
    vectors = embeddingModelName.embed_documents(text)
    client.upsert(
        # creating collections for storing embeddings
        collectionName = "DocumentCollections",
        # qdrant points consists of id, vector and payload
        points = [
            PointStruct(
                id = docID,
                vector = vectors,
                payload = {"text": text}
            )
        ]
    )