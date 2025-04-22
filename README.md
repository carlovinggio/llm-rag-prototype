# Azure AI Search + FastAPI Q&A Prototype

## Overview
This prototype accepts a natural language question via CLI or HTTP, retrieves relevant documents from Azure AI Search, and generates a concise answer using OpenAI.

## Prerequisites
- Python 3.10+
- Azure Cognitive Search instance with an index named in `AZURE_SEARCH_INDEX_NAME`
- OpenAI API key

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/azure-ai-search-fastapi-prototype.git
   cd azure-ai-search-fastapi-prototype
