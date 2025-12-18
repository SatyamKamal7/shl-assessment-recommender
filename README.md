# SHL Assessment Recommendation Engine

This project builds an LLM-powered RAG system that recommends SHL assessments
based on natural language queries.

## Features
- SHL catalogue scraping
- Semantic search using embeddings
- FastAPI-based recommendation API
- Evaluation using Precision@K

## Run API
uvicorn api.main:app --reload