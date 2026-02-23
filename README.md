🚀 Advanced Hybrid RAG System (1M+ Scale)

Production-grade Retrieval-Augmented Generation (RAG) backend engineered for low-latency, high-precision semantic search at million-scale.

Designed to simulate a realistic enterprise deployment with strict latency and cost constraints.

🔥 Core Features

Hybrid Retrieval (Dense + BM25)

HNSW ANN Indexing via Qdrant

Cross-Encoder Re-Ranking

Multi-Level Caching with Redis

Prompt Injection Guardrails

Sub-10ms Warm Query Latency

Designed for 1M+ embeddings

🏗 System Architecture
User Query
   ↓
Guardrails Layer
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
Score Fusion (Weighted)
   ↓
Cross-Encoder Re-Ranking
   ↓
Final Top-K Results
☁ Infrastructure

The system was deployed on an Microsoft Azure Virtual Machine.

VM Configuration

Instance: D4s_v3

4 vCPUs

16 GB RAM

Premium SSD

Ubuntu 22.04

Containerized Components

All services run via Docker:

Qdrant (Vector Database)

Redis (Multi-Level Cache)

FastAPI backend

Embedding + Re-ranking services

This setup simulates a production-style cloud backend under realistic compute constraints.

📊 Scale Design

1M+ embeddings

384-dimensional vectors

Cosine similarity metric

HNSW Configuration

m = 32

ef_construct = 200

ef_search tuned dynamically based on recall/latency tradeoff

Retrieval Strategy

Two-stage retrieval pipeline

Dense + Sparse fusion (weighted scoring)

Cross-encoder re-ranking for final precision

Redis LRU caching for hot queries

Memory-optimized ANN indexing

⚡ Latency Benchmarking

Latency was measured using:

time.perf_counter() in Python

100-query average benchmarking

Separate cold vs warm query evaluation

End-to-end measurement (API entry → final response)

Cold Query

Includes:

Embedding generation

ANN search

BM25 retrieval

Cross-encoder re-ranking

Average latency: 40–55 ms

Warm Query

Cache hit:

Query cached

Embedding cached

ANN search reused

Average latency: 5–10 ms

Measurement Method
start = time.perf_counter()
# run retrieval pipeline
end = time.perf_counter()
latency_ms = (end - start) * 1000

Results averaged across multiple runs to remove outliers.

🎯 Design Principles

This project focuses on:

Retrieval quality before generation

ANN parameter tuning for scale

Cache-aware system design

Cost-efficient cloud deployment

Guardrails-first architecture

At enterprise scale, architecture decisions matter more than model choice.
