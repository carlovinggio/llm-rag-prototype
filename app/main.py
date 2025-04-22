import os
import argparse
import uvicorn
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI for Q&A prototype")
    parser.add_argument("question", help="Natural language question")
    args = parser.parse_args()
    print(retrieve_and_answer(args.question))
