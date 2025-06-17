# ai-ecommerce-agent

An AI-powered shopping assistant leveraging FastAPI, AutoGen, and Ollama with a React ChatUI frontend. The agent can search the product catalog using FAISS embeddings and interact with GrandNode to manage carts and orders.

## Running Locally

1. Copy `.env.template` to `.env` and adjust values if needed.
2. Build and start all services:

```bash
docker-compose up --build
```

- Frontend: <http://localhost:3000>
- Backend: <http://localhost:8000>
- GrandNode: <http://localhost:5000>
- Ollama: <http://localhost:11434>

## Embedding the Product Catalog

Run the FAISS loader inside the backend container to generate an index from the GrandNode MongoDB:

```bash
python backend/tools/faiss_loader.py
```

This stores vectors in `faiss.index` which the agent uses for product retrieval.

## Testing the Chat Flow

Open the frontend and ask questions such as:

- "Compare the Commander and Z-10 models"
- "Find a rake for a 2-acre property with wet leaves"
- "Add Commander to my cart"
- "Place the order with standard shipping"
- "Where's my order CYL45678?"

The backend `/agent` endpoint handles chat messages and communicates with GrandNode.

## Connecting to GrandNode

The backend talks to GrandNode via REST API defined in `grandnode_client.py`. Update the `GRANDNODE_URL` environment variable if GrandNode runs elsewhere. The MongoDB connection string is set with `MONGO_URI`.
