from fastapi import FastAPI

app = FastAPI(title="Wikipedia Search Engine", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Wikipedia Search Engine API"}

@app.get("/search")
async def search(q: str):
    return {"query": q, "results": []}