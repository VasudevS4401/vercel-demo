# api/index.py
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()

marks_data = {
    "Alice": 90,
    "Bob": 85,
    "FYgbkNaLi": 77,
    "Charlie": 92
}

@app.get("/api")
def get_marks(name: List[str] = Query([])):
    results = [marks_data.get(n, "Not Found") for n in name]
    return JSONResponse(content={"results": results})
