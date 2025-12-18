import faiss, json
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("data/shl.index")

with open("data/shl_catalogue.json") as f:
    catalogue = json.load(f)

def recommend(query, k=3):
    q_emb = model.encode([query])
    _, idx = index.search(np.array(q_emb), k)

    results = []
    for i in idx[0]:
        results.append({
            "assessment": catalogue[i]["assessment_name"],
            "reason": "Strong semantic match with the query"
        })
    return results