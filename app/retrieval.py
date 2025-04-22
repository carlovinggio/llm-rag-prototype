from app.azure_search import search_documents
from app.llm import caller


def retrieve_and_answer(question: str) -> str:
    docs = search_documents(question)
    context = "\n".join([d["content"] for d in docs])
    prompt = "Answer the question based on the context provided. \n\nContext:\n{context}\n\nQuestion: {question}"
    prompt = prompt.format(context=context, question=question)
    return caller(prompt)
