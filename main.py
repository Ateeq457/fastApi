from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import random
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load quotes from file
with open("quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)

@app.get("/quotes")
def get_quotes(category: str = Query("All"), limit: int = Query(10)):
    pool = quotes if category.lower() == "all" else [
        q for q in quotes if q["category"].lower() == category.lower()
    ]
    return random.sample(pool, min(limit, len(pool)))
