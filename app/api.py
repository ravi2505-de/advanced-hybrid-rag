from fastapi import FastAPI
from app.guardrails import validate_query
from app.embeddings import get_embedding
from app.hybrid_retriever import hybrid_search
from app.reranker import rerank
from app.cache import get_query_cache, set_query_cache

app = FastAPI()

@app.get("/search")
def search(query: str):
    validate_query(query)

    cached = get_query_cache(query)
    if cached:
        return {"cached": True, "results": cached}

    embedding = get_embedding(query)
    results = hybrid_search(query, embedding)

    doc_texts = [f"Document {r[0]}" for r in results]
    final_results = rerank(query, doc_texts)

    set_query_cache(query, final_results)

    return {"cached": False, "results": final_results}