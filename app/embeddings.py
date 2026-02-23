from sentence_transformers import SentenceTransformer
from app.cache import get_embedding_cache, set_embedding_cache

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(query: str):
    cached = get_embedding_cache(query)
    if cached:
        return cached

    embedding = model.encode(query).tolist()
    set_embedding_cache(query, embedding)
    return embedding