
from app.azure_search import upload_data
import json

def uploader():
    """
    Uploads data to Azure Search.
    """
    data_filename = "sample_data/tax_policies.json"

    with open(data_filename, "r") as f:
        data = json.load(f)
        upload_data(data)


if __name__ == "__main__":
    uploader()
