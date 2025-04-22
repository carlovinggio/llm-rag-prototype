
import os
from langchain_openai import ChatOpenAI

default_model = "gpt-4o"
openai_credential = os.environ["OPENAI_API_KEY"]

def caller(prompt: str, model=default_model) -> str:
    model = ChatOpenAI(model=default_model, api_key=openai_credential)
    return model.invoke(prompt).content
