from app.embeddings import get_embeddings
import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import uuid

endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
api_key = os.getenv("AZURE_SEARCH_API_KEY")
index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")

def get_search_client(index_nm: str):
    return SearchClient(
        endpoint=endpoint,
        index_name=index_nm,
        credential=AzureKeyCredential(api_key)
    )


def search_documents(query: str, index_nm: str = index_name, top_k: int = 3):
    client = get_search_client(index_nm)
    results = client.search(
        search_text=query,
        top=top_k
    )
    docs = []
    for r in results:
        docs.append({
            "id": r["id"],
            "content": r.get("content", "")
        })
    return docs


def upload_data(data_list: list[str]):
    client = get_search_client()
    batch = []
    embeddings = get_embeddings()
    for data in data_list:
        vector = embeddings.embed_query(data)
        batch.append({
            "id": str(uuid.uuid4()),
            "content": data,
            "content_vector": vector
        })
    client.upload_documents(documents=batch)
