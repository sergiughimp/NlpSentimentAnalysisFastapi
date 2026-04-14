# Sentiment Analysis API

A REST API that classifies the emotional tone of input text using VADER sentiment analysis.

## Setup

Create and activate a virtual environment before installing dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m nltk.downloader vader_lexicon
python -m pytest tests/ -v
```

## Run

```bash
python -m uvicorn app.main:app --reload
```

> **Note:** Use `python -m uvicorn` rather than `uvicorn` directly to ensure the server and its reload subprocess both use the virtual environment's Python interpreter.

Then visit: http://127.0.0.1:8000/docs for the interactive API documentation.

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Health check — confirms the API is running |
| POST | `/analyse` | Classify sentiment of submitted text |
| GET | `/stats` | Return aggregate sentiment statistics across all requests |

### `GET /`

```json
{
  "message": "Sentiment Analysis API is running. Visit /docs for the interactive API documentation."
}
```

### `POST /analyse`

Request body:

```json
{
  "text": "The service was quick and friendly."
}
```

Response body:

```json
{
  "text": "The service was quick and friendly.",
  "label": "positive",
  "score": 0.7269
}
```

- `label` is one of `positive`, `negative`, `neutral`
- `score` is VADER compound score in range `[-1.0, 1.0]`

### `GET /stats`

Returns in-memory aggregates from all requests made since the process started:

```json
{
  "total_requests": 3,
  "average_score": 0.1212,
  "label_counts": {
    "positive": 1,
    "negative": 1,
    "neutral": 1
  }
}
```

The API does **not** persist requests; restarting the server resets all stats.

## Tests

```bash
pytest tests/ -v
```

## Example

```bash
curl -X POST http://127.0.0.1:8000/analyse \
     -H "Content-Type: application/json" \
     -d '{"text": "The staff were incredibly helpful and kind"}'

curl http://127.0.0.1:8000/stats
```

## Project Structure

```
sentiment-analysis-api/
├── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI app and routing
│   ├── schemas.py     # Pydantic request/response models
│   └── store.py       # In-memory aggregation store
├── model/
│   ├── __init__.py
│   └── predict.py     # VADER sentiment model
├── tests/
│   ├── __init__.py
│   └── test_api.py    # Integration and unit tests
├── requirements.txt
├── .gitignore
└── README.md
```