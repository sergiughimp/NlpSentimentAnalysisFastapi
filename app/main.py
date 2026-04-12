from fastapi import FastAPI
from app.schemas import AnalyseRequest, AnalyseResponse, StatsResponse

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
    return {"total_requests": 0, "average_score": 0.0, "label_counts": {}}