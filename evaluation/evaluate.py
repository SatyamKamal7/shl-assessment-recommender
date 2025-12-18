def precision_at_k(predicted, expected, k=3):
    hits = sum(1 for p in predicted[:k] if p in expected)
    return hits / k