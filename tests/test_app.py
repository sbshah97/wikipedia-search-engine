"""Tests for the FastAPI application."""

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.main import app

# Create test client
client = TestClient(app)


def test_root_endpoint() -> None:
    """Test the root endpoint returns expected message."""
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert data["message"] == "Wikipedia Search Engine API"


def test_search_endpoint_with_query() -> None:
    """Test the search endpoint with a query parameter."""
    query = "python programming"
    response = client.get(f"/search?q={query}")
    assert response.status_code == 200

    data = response.json()
    assert "query" in data
    assert "results" in data
    assert data["query"] == query
    assert isinstance(data["results"], list)
    assert data["results"] == []  # Currently returns empty results


def test_search_endpoint_with_different_queries() -> None:
    """Test the search endpoint with various query parameters."""
    test_queries = [
        "machine learning",
        "artificial intelligence",
        "data science",
        "web development",
        "123",
        "a",
        "test with spaces and symbols!@",
    ]

    for query in test_queries:
        response = client.get(f"/search?q={query}")
        assert response.status_code == 200

        data = response.json()
        assert data["query"] == query
        assert isinstance(data["results"], list)


def test_search_endpoint_url_encoding() -> None:
    """Test the search endpoint with URL-encoded query parameters."""
    query = "machine learning & AI"
    response = client.get("/search", params={"q": query})
    assert response.status_code == 200

    data = response.json()
    assert data["query"] == query


def test_search_endpoint_missing_query() -> None:
    """Test the search endpoint without query parameter."""
    response = client.get("/search")
    # Should return 422 Unprocessable Entity for missing required parameter
    assert response.status_code == 422


def test_search_endpoint_empty_query() -> None:
    """Test the search endpoint with empty query parameter."""
    response = client.get("/search?q=")
    assert response.status_code == 200

    data = response.json()
    assert data["query"] == ""
    assert isinstance(data["results"], list)


@pytest.mark.asyncio
async def test_async_client_root_endpoint() -> None:
    """Test the root endpoint using async client."""
    from httpx import ASGITransport

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/")

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Wikipedia Search Engine API"


@pytest.mark.asyncio
async def test_async_client_search_endpoint() -> None:
    """Test the search endpoint using async client."""
    from httpx import ASGITransport

    query = "async test"
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get(f"/search?q={query}")

    assert response.status_code == 200
    data = response.json()
    assert data["query"] == query
    assert isinstance(data["results"], list)


def test_app_metadata() -> None:
    """Test that the FastAPI app has correct metadata."""
    assert app.title == "Wikipedia Search Engine"
    assert app.version == "1.0.0"


def test_nonexistent_endpoint() -> None:
    """Test that non-existent endpoints return 404."""
    response = client.get("/nonexistent")
    assert response.status_code == 404
