from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Load JSON once at startup
json_path = os.path.join(os.path.dirname(__file__), "marks.json")
with open(json_path, "r") as file:
    marks_data = json.load(file)

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    result = [marks_data.get(name, None) for name in names]
    return JSONResponse(content={"marks": result})

