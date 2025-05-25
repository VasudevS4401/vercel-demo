from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Make sure path is correct relative to this file
json_path = os.path.join(os.path.dirname(__file__), "marks.json")

with open(json_path, "r") as file:
    data = json.load(file)

@app.get("/api")
def get_marks(name: list[str] = []):
    results = []
    for n in name:
        for entry in data:
            if entry["name"] == n:
                results.append({"name": n, "marks": entry["marks"]})
                break
        else:
            results.append({"name": n, "marks": None})  # Not found
    return {"results": results}
