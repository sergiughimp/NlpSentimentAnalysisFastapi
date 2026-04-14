from fastapi import FastAPI
from app.schemas import AnalyseRequest, AnalyseResponse, StatsResponse
from app.store import store
from model.predict import predict

app = FastAPI(
    title="Sentiment Analysis API",
    description=(
        "A REST API that classifies the emotional tone of input text. "
        "Sentiment scores are returned per request, and aggregate statistics "
        "are available across all requests made since the server started."
    ),
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "Sentiment Analysis API is running. Visit /docs for the interactive API documentation."}

@app.post(
    "/analyse",
    response_model=AnalyseResponse,
    summary="Analyse sentiment of text",
    description=(
        "Submits a string of text for sentiment classification. "
        "Returns a label (positive, negative, or neutral) and a "
        "confidence score between -1.0 and 1.0."
    ),
)
def analyse(request: AnalyseRequest):
    result = predict(request.text)
    store.record(result["label"], result["score"])
    return {"text": request.text, "label": result["label"], "score": result["score"]}

@app.get(
    "/stats",
    response_model=StatsResponse,
    summary="Get aggregate sentiment statistics",
    description=(
        "Returns the total number of requests made since the server started, "
        "the average sentiment score across all requests, and a breakdown of "
        "how many requests returned each label. Data is not persisted — "
        "statistics reset when the server restarts."
    ),
)
def stats():
    return {
        "total_requests": store.total_requests,
        "average_score": store.average_score(),
        "label_counts": store.label_counts,
    }