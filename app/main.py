from fastapi import FastAPI

app = FastAPI(
    title="Sentiment Analysis API",
    description="Classifies the emotional tone of input text.",
    version="1.0.0",
)

@app.post("/analyse")
def analyse():
    return {"message": "stub"}

@app.get("/stats")
def stats():
    return {"message": "stub"}