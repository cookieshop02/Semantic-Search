from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient(path="qdrant_db")

collection = "internet_docs"

def create_collection():
    client.recreate_collection(collection_name=collection, vectors_config = VectorParams(size=384, distance=Distance.COSINE))


def search(query_vector):
    results = client.query_points(collection_name=collection,query=query_vector,limit=3)
    
    docs = []

    for point in results.points:
        payload = point[1] if isinstance(point, tuple) else point.payload
        docs.append(payload["text"])

    return docs