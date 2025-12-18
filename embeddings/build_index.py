import json
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/shl_catalogue.json") as f:
    data = json.load(f)

texts = [d["assessment_name"] + " " + d["description"] for d in data]
embeddings = model.encode(texts)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

faiss.write_index(index, "data/shl.index")