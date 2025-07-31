# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Wikipedia Search Engine built from scratch to demonstrate deep understanding of information retrieval systems. The project serves as a comprehensive learning platform for mastering search engineering skills required at companies like Perplexity and Google.

**Current Focus**: Building an inverted index on Wikipedia dataset (Milestone 1)

## Architecture

- **FastAPI Application**: Located in `app/main.py` - main API server with search endpoints
- **Entry Point**: `main.py` in root - simple CLI entry point 
- **Package Management**: Uses `uv` for dependency management (evidenced by `uv.lock` file)
- **Search Engine Components**: Will be built incrementally starting with inverted index

## Key Files

- `app/main.py` - FastAPI application with `/` and `/search` endpoints
- `main.py` - Simple CLI entry point that prints a hello message
- `pyproject.toml` - Project configuration with FastAPI dependencies
- `requirements.txt` - Auto-generated dependency list from uv

## Development Commands

### Running the Application
```bash
# Run the FastAPI server
uvicorn app.main:app --reload

# Run the CLI version
python main.py
```

### Dependency Management
```bash
# Install dependencies
uv sync

# Add new dependency
uv add <package-name>

# Export requirements
uv export --format requirements-txt > requirements.txt
```

## Development Roadmap

### Milestone 1: Inverted Index (Current Focus)
- Build inverted index from Wikipedia dataset
- Implement document preprocessing (tokenization, stemming, stop words)
- Create term-to-document mappings
- Design memory-efficient storage format

### Future Milestones
- Ranking algorithms (TF-IDF, BM25)
- Neural retrieval with transformers
- Distributed architecture and scaling
- RAG pipeline integration

## Current State

The project currently has:
- Basic FastAPI setup with title "Wikipedia Search Engine" 
- Root endpoint returning API info
- Search endpoint `/search?q=<query>` that accepts query parameter but returns empty results
- Dependencies: FastAPI, uvicorn, python-multipart

**Next Steps**: Implement inverted index construction from Wikipedia dataset to enable actual search functionality.