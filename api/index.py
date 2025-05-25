from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

json_path = os.path.join(os.path.dirname(__file__), "marks.json")
with open(json_path, "r") as file:
    data = json.load(file)

@app.get("/api")
def get_marks(name: List[str] = Query([])):
    # Create a lookup dict for fast access
    marks_lookup = {entry["name"]: entry["marks"] for entry in data}

    # Collect marks in the order of input names
    result_marks = [marks_lookup.get(n, None) for n in name]

    return {"marks": result_marks}
