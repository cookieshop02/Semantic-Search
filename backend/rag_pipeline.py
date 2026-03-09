from embedding import embedding_model
from vector_store import search
from llm import generate_response

def ask_rag(question):

    # question -> embedding
    query_vector = embedding_model(question)

    # embedding -> search in vector db -> relevant docs
    docs = search(query_vector)

    #combine retrieved context
    context = "\n\n".join(docs)

    # question + context -> llm -> answer
    answer = generate_response(context, question)

    return answer