from embedding import embedding_model
from vector_store import search

query = "How does DNS work?"

vector = embedding_model(query)

results = search(vector)

print(results)