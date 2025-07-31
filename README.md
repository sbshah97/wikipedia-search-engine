# Wikipedia Search Engine

A comprehensive search engine built from scratch to demonstrate deep understanding of information retrieval systems, machine learning, and distributed computing. This project serves as a learning platform for mastering the technical skills required for senior search engineering roles at companies like Perplexity, Google, and other search-focused organizations.

## <� Learning Objectives

This project is designed to build expertise in:

- **Core Search Technologies**: Inverted indexes, ranking algorithms (TF-IDF, BM25), query processing
- **Modern ML Approaches**: Neural retrieval, transformer-based embeddings, hybrid search systems
- **Distributed Systems**: Horizontal scaling, sharding, distributed consensus
- **RAG Pipelines**: Integration with large language models for contextual answer generation
- **Performance Engineering**: Latency optimization, caching strategies, system profiling

## <� Architecture Roadmap

### Phase 1: Core Search Engine (Current)
-  Basic FastAPI structure
- = Inverted index implementation
- = TF-IDF and BM25 ranking
- = Query processing pipeline

### Phase 2: Neural Retrieval
- Dense vector search with BERT/Sentence-BERT
- Bi-encoder architectures for semantic matching
- Hybrid lexical + semantic search fusion

### Phase 3: Distributed & Scalable
- Sharded index architecture
- Query routing and load balancing
- Incremental index updates

### Phase 4: RAG Integration
- LLM integration for answer generation
- Context-aware response synthesis
- Answer quality evaluation metrics

## =� Getting Started

### Prerequisites
- Python 3.10+
- uv (for dependency management)

### Installation
```bash
# Clone the repository
git clone <repo-url>
cd wikipedia-search-engine

# Install dependencies
uv sync

# Run the development server
uvicorn app.main:app --reload
```

### API Endpoints
- `GET /` - API information
- `GET /search?q=<query>` - Search Wikipedia articles (currently returns empty results)

## =� Dataset

This project uses Wikipedia articles as the primary dataset for indexing and search. The choice of Wikipedia provides:
- Large-scale, real-world text data
- Structured content with metadata
- Multilingual capabilities for future expansion
- Well-understood domain for evaluation

## =� Technology Stack

- **Backend**: FastAPI (Python) - rapid prototyping and ML integration
- **Performance-Critical Components**: Planned migration to Rust/C++ for indexing and retrieval
- **ML/AI**: Transformers, PyTorch/TensorFlow for neural models
- **Infrastructure**: Docker, Kubernetes for scalable deployment
- **Monitoring**: Comprehensive logging and performance metrics

## =� Success Metrics

- **Relevance**: NDCG@10, MAP, MRR on standard IR benchmarks
- **Performance**: Query latency < 100ms, index build time optimization
- **Scalability**: Handle 10M+ documents with sub-second response times
- **Learning**: Document architecture decisions and trade-offs for interview discussions

## <� Educational Value

This project demonstrates:
1. **Systems Thinking**: End-to-end search pipeline design
2. **ML Engineering**: From classical IR to modern neural approaches
3. **Performance Engineering**: Optimization at scale
4. **Research Application**: Implementing and improving upon academic papers
5. **Interview Preparation**: Concrete examples for senior engineering discussions

## =, Research Areas

Future exploration includes:
- Learning-to-rank with gradient boosting
- Sparse retrieval models (SPLADE, ColBERT)
- Multi-modal search capabilities
- Real-time index updates and consistency
- Query understanding and intent classification

## =� License

MIT License - see LICENSE file for details

---

*Building this search engine from first principles provides the deep technical understanding that distinguishes senior engineers in the search and information retrieval domain.*