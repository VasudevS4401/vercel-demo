from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Load the JSON file
def load_marks():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_dir, "marks.json")) as f:
        return json.load(f)

data = load_marks()

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    results = []
    for name in names:
        # Search through the list for matching name
        mark_entry = next((item for item in data if item["name"] == name), None)
        if mark_entry:
            results.append(mark_entry["marks"])
        else:
            results.append(None)  # or 0, or -1, or "not found"
    return JSONResponse(content={"marks": results})
