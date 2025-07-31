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

# Install with development dependencies
uv sync --dev

# Add new dependency
uv add <package-name>

# Add development dependency
uv add --dev <package-name>

# Export requirements
uv export --format requirements-txt > requirements.txt
```

### Code Quality Tools

This project uses modern Python tooling for code quality and consistency:

#### Ruff - Ultra-fast Python Linter & Formatter
```bash
# Run linting checks
uv run ruff check .

# Auto-fix issues where possible
uv run ruff check --fix .

# Format code
uv run ruff format .

# Check formatting without changes
uv run ruff format --check .
```

#### MyPy - Static Type Checker
```bash
# Run type checking
uv run mypy .

# Type check specific file
uv run mypy app/main.py
```

### CI/CD Pipeline

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that automatically:
- Runs on push to main and feature branches
- Runs on pull requests to main
- Sets up Python 3.13 environment
- Installs dependencies with uv
- Runs Ruff linting and formatting checks
- Runs MyPy type checking
- Tests application startup (both CLI and FastAPI server)

The CI pipeline uses parallel jobs for efficiency and caches dependencies for faster builds.

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
- **Modern Development Setup**:
  - Python 3.13 with strict type checking
  - Ruff for ultra-fast linting and formatting
  - MyPy for static type analysis
  - Comprehensive .gitignore for Python/FastAPI projects
  - GitHub Actions CI/CD pipeline with automated quality checks

## Development Workflow

1. **Make changes** to code in feature branch
2. **Run quality checks locally**:
   ```bash
   uv run ruff check --fix .
   uv run ruff format .
   uv run mypy .
   ```
3. **Commit and push** - CI will automatically run the same checks
4. **Create pull request** to main branch
5. **Merge only after** all CI checks pass

**Next Steps**: Implement inverted index construction from Wikipedia dataset to enable actual search functionality.