import os
from typing import List

import faiss
from sentence_transformers import SentenceTransformer
from pymongo import MongoClient

INDEX_FILE = os.environ.get("FAISS_INDEX", "faiss.index")
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017")
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def load_products() -> List[str]:
    """Fetch product titles and descriptions from MongoDB."""
    client = MongoClient(MONGO_URI)
    db = client.get_default_database()
    products = []
    for item in db.Product.find({}, {"Name": 1, "ShortDescription": 1}):
        text = f"{item.get('Name', '')} {item.get('ShortDescription', '')}"
        products.append(text)
    return products


def build_faiss_index(texts: List[str]) -> None:
    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(texts)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    faiss.write_index(index, INDEX_FILE)


def main() -> None:
    texts = load_products()
    if not texts:
        print("No products found")
        return
    build_faiss_index(texts)
    print(f"Stored {len(texts)} products in {INDEX_FILE}")


if __name__ == "__main__":
    main()
