# api/index.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import csv
import os

app = FastAPI()

# Load CSV once at startup
marks_data = {}
csv_path = os.path.join(os.path.dirname(__file__), "marks.csv")
with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        marks_data[row["name"]] = int(row["marks"])

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    result = [marks_data.get(name, None) for name in names]
    return JSONResponse(content={"marks": result})

