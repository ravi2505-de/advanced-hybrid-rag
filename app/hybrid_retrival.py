from qdrant_client import QdrantClient
from rank_bm25 import BM25Okapi
from app.config import *
import numpy as np

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

documents = []
tokenized_docs = []
bm25 = None

def initialize_bm25(docs):
    global documents, tokenized_docs, bm25
    documents = docs
    tokenized_docs = [doc.split() for doc in docs]
    bm25 = BM25Okapi(tokenized_docs)

def hybrid_search(query, embedding):
    dense_results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=embedding,
        limit=TOP_K
    )

    sparse_scores = bm25.get_scores(query.split())
    
    combined = []
    for idx, result in enumerate(dense_results):
        dense_score = result.score
        sparse_score = sparse_scores[result.id]
        final_score = 0.7 * dense_score + 0.3 * sparse_score
        combined.append((result.id, final_score))

    combined.sort(key=lambda x: x[1], reverse=True)
    return combined[:TOP_K]