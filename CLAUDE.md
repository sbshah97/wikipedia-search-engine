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

## Key Learnings from Modern Python Development Setup

### Tool Selection and Configuration
- **Ruff over traditional linters**: Chose Ruff over flake8/black/isort combination for 10-100x performance improvement
- **Strict MyPy configuration**: Enabled strict mode for maximum type safety, crucial for large-scale search systems
- **Python 3.13+ features**: Used modern type annotations (`dict[str, Any]` vs `typing.Dict`) for cleaner code
- **uv for dependency management**: Fast, reliable alternative to pip/poetry with excellent lock file support

### CI/CD Best Practices
- **Parallel job execution**: Separated linting and testing into parallel jobs for faster feedback
- **Dependency caching**: Used `astral-sh/setup-uv@v4` with caching for 2-3x faster CI runs
- **Feature branch workflows**: Configured CI to run on both feature branches and PRs for early feedback
- **Comprehensive testing**: Added both CLI and FastAPI server startup tests to catch integration issues

### Code Quality Standards
- **Type annotations everywhere**: All functions have proper return type annotations for better IDE support
- **Modern Python syntax**: Leveraged Python 3.13+ features like improved type hints
- **Comprehensive linting rules**: Enabled 10+ rule categories covering bugs, style, complexity, and upgrades
- **Per-file ignore patterns**: Strategic ignoring of rules where appropriate (e.g., no type annotations in tests)

### Development Workflow Improvements
- **Local-first development**: Developers can run same checks locally before pushing
- **Automated formatting**: Ruff auto-fixes many issues, reducing manual work
- **Fast feedback loops**: Ruff checks complete in seconds vs minutes with traditional tools
- **Documentation integration**: All commands documented in CLAUDE.md for easy reference

### FastAPI-Specific Optimizations
- **Import ordering**: Configured isort to understand FastAPI project structure
- **Type safety with Pydantic**: MyPy configuration ready for Pydantic model validation
- **Async function support**: Proper type annotations for async FastAPI endpoints
- **Development server testing**: CI validates both production and development server startup

### Project Architecture Benefits
- **Scalability preparation**: Strict typing and linting prepare codebase for complex search algorithms
- **Team collaboration**: Consistent code style and quality checks enable multiple contributors
- **Interview readiness**: Professional tooling demonstrates software engineering best practices
- **Maintenance efficiency**: Automated quality checks reduce technical debt accumulation

### GitHub Integration Best Practices
- **Pull Request Automation**: Successfully used `gh pr create` with comprehensive description templates
- **Repository Protection Rules**: Learned about branch protection requiring PRs for all changes
- **CI Integration**: GitHub Actions automatically runs on PR creation, preventing bad merges
- **Merge Strategies**: Repository configured for squash merges to maintain clean history

## GitHub Integration

### Pull Request Management
```bash
# Create PR using GitHub CLI
gh pr create --title "Title" --body "Description"

# View PR status
gh pr status

# Merge PR after CI passes (if you have permissions)
gh pr merge --squash

# View PR details
gh pr view <number>
```

**Next Steps**: Implement inverted index construction from Wikipedia dataset to enable actual search functionality.