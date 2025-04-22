# Azure AI Search + FastAPI Q&A Prototype

## Overview
This prototype accepts a natural language question via HTTP, retrieves relevant documents from Azure AI Search, and generates a concise answer using OpenAI.

## Prerequisites
- Python 3.10+
- Azure Cognitive Search instance with an index named in `AZURE_SEARCH_INDEX_NAME`
- OpenAI API key

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/carlovinggio/llm-rag-prototype.git
   cd llm-rag-prototype

2. Install the requirements
    You could either create an environment and install the requirements from 'requirements.txt' or make a 'docker-compose up --build'

3. Since we are using azure ai search you need to use the 'app/db_definition.json' into the creation of a Azure AI Search DB

4. Define the environment variables, you could use the .env.sample, but rename it as .env
    - AZURE_SEARCH_ENDPOINT
    - AZURE_SEARCH_API_KEY
    - AZURE_SEARCH_INDEX_NAME
    - OPENAI_API_KEY

5. Setting up the sample data
    execute the script 'sample_data/upload_data.py', you could add more tax_policies

6. Make the query:
    - You can execute the 'app/main.py' script with the query you want
    - After making the 'docker-compose up --build' you can open 'http://0.0.0.0:8000/docs#/default/query_query_post' and execute the query endpoint


Consider that AZURE has free services (basic ones) that you can easily setup 
Bonus:
In order demonstrate multi-source retrieval, when calling the "search_documents" function you can set the index name

