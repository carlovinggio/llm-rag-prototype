from fastapi import FastAPI
from pydantic import BaseModel
from app.retrieval import retrieve_and_answer

class Query(BaseModel):
    question: str

app = FastAPI()

@app.post("/query")
def query(q: Query):
    answer = retrieve_and_answer(q.question)
    return {"question": q.question, "answer": answer}
