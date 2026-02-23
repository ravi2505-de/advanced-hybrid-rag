import redis
import json
import hashlib
from app.config import REDIS_HOST, REDIS_PORT, CACHE_TTL

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def _hash(text: str):
    return hashlib.sha256(text.encode()).hexdigest()

def get_query_cache(query: str):
    key = f"query:{_hash(query)}"
    data = r.get(key)
    return json.loads(data) if data else None

def set_query_cache(query: str, value):
    key = f"query:{_hash(query)}"
    r.setex(key, CACHE_TTL, json.dumps(value))

def get_embedding_cache(query: str):
    key = f"embedding:{_hash(query)}"
    data = r.get(key)
    return json.loads(data) if data else None

def set_embedding_cache(query: str, embedding):
    key = f"embedding:{_hash(query)}"
    r.setex(key, CACHE_TTL, json.dumps(embedding))