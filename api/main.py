from fastapi import FastAPI
from rag.recommender import recommend

app = FastAPI()

@app.post("/recommend")
def get_recommendation(payload: dict):
    query = payload["query"]
    return {"recommendations": recommend(query)}