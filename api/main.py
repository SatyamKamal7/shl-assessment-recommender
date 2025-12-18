from fastapi import FastAPI
from rag.recommender import recommend

app = FastAPI(title="SHL Assessment Recommendation API")

@app.get("/")
def health():
    return {"status": "API is running"}

@app.post("/recommend")
def get_recommendation(payload: dict):
    query = payload["query"]
    return {"recommendations": recommend(query)}