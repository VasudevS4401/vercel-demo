import json
import os
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()

# Read the marks.json using a safe path
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "marks.json")

with open(json_path, "r") as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(name: List[str] = Query([])):
    results = [marks_data.get(n, "Not Found") for n in name]
    return JSONResponse(content={"results": results})
