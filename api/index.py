from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS: Allow all origins (for demo/testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods, including GET
    allow_headers=["*"]
)

# Load the marks data once on startup
with open("marks.json", "r") as file:
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
    return {"marks": results}
