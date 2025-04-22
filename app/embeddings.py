import os

from langchain_openai import OpenAIEmbeddings


def get_embeddings():
    DIMENSIONS = int(os.environ.get("DIMENSIONS", 1024))
    embeddings = OpenAIEmbeddings(
        dimensions=DIMENSIONS, model="text-embedding-3-large"
    )
    return embeddings
