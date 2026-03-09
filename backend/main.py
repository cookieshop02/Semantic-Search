from fastapi import FastAPI
from rag_pipeline import ask_rag

app = FastAPI()

@app.get("/")
def  home():
    return{"message": "Hello buddies!"}

@app.post("/ask")
def ask(question: str):
    answer = ask_rag(question)
    return {"answer": answer}
