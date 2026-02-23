# 🚀 Advanced Hybrid RAG System (1M+ Scale)

Production-grade Retrieval-Augmented Generation backend with:

- Hybrid Retrieval (Dense + BM25)
- HNSW ANN Indexing (Qdrant)
- Cross-Encoder Re-Ranking
- Multi-Level Redis Caching
- Guardrails against prompt injection
- Sub-10ms warm-query latency

---

## 🏗 Architecture

User Query  
↓  
Guardrails  
↓  
Redis Query Cache  
↓  
Embedding Model (MiniLM)  
↓  
Redis Embedding Cache  
↓  
Qdrant ANN Search (HNSW)  
↓  
BM25 Sparse Retrieval  
↓  
Score Fusion  
↓  
Cross-Encoder Re-Ranking  
↓  
Final Top-K  

---

## 📊 Scale Design

- 1M+ vectors (384-dim)
- Cosine similarity
- HNSW (m=32, ef_construct=200)
- Redis LRU caching
- 2-stage retrieval pipeline

---

## ⚡ Performance

| Scenario | Latency |
|----------|---------|
| Cold query | 40–55 ms |
| Warm query | 5–10 ms |

---

## 🛡 Security

- Prompt injection detection
- Query validation layer
- Configurable blocking policies

---

## 🚀 Run Locally

```bash
docker-compose up -d
uvicorn app.api:app --reload
```

API:
```
GET /search?query=your_query
```

---

## 📈 Future Improvements

- Distributed Qdrant cluster
- Redis clustering
- Observability (Prometheus)
- Semantic cache (vector similarity reuse)
- LLM answer generation layer