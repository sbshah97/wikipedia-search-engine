from typing import Any

from fastapi import FastAPI

app = FastAPI(title="Wikipedia Search Engine", version="1.0.0")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Wikipedia Search Engine API"}


@app.get("/search")
async def search(q: str) -> dict[str, Any]:
    return {"query": q, "results": []}
