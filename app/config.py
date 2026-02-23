import os

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = 6333
COLLECTION_NAME = "hybrid_rag_collection"

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = 6379

TOP_K = 20
FINAL_K = 5
CACHE_TTL = 600