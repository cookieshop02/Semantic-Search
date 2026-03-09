from embedding import embedding_model
from vector_store import create_collection, client, collection
from qdrant_client.models import PointStruct

with open("../data/internet_docs.txt", "r") as f:
    docs = f.read().split("\n\n")

create_collection()

point = []

for i, doc in enumerate(docs):
    
    vector = embedding_model(doc).tolist()

    point.append(
        PointStruct(
            id=i,
            vector=vector,
            payload={"text": doc}
        )
    )

client.upsert(
    collection_name=collection,
    points=point
)

print("Documents inserted into vector database")