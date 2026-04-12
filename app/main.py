from fastapi import FastAPI
from app.schemas import AnalyseRequest, AnalyseResponse, StatsResponse
from app.store import store
from model.predict import predict

app = FastAPI(
    title="Sentiment Analysis API",
    description="Classifies the emotional tone of input text.",
    version="1.0.0",
)

@app.post("/analyse", response_model=AnalyseResponse)
def analyse(request: AnalyseRequest):
    result = predict(request.text)
    store.record(result["label"], result["score"])
    return {"text": request.text, "label": result["label"], "score": result["score"]}

@app.get("/stats", response_model=StatsResponse)
def stats():
    return {
        "total_requests": store.total_requests,
        "average_score": store.average_score(),
        "label_counts": store.label_counts,
    }