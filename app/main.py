from fastapi import FastAPI
from app.schemas import AnalyseRequest, AnalyseResponse, StatsResponse
from app.store import store

app = FastAPI(
    title="Sentiment Analysis API",
    description="Classifies the emotional tone of input text.",
    version="1.0.0",
)

@app.post("/analyse", response_model=AnalyseResponse)
def analyse(request: AnalyseRequest):
    return {"text": request.text, "label": "stub", "score": 0.0}

@app.get("/stats", response_model=StatsResponse)
def stats():
    return {
        "total_requests": store.total_requests,
        "average_score": store.average_score(),
        "label_counts": store.label_counts,
    }