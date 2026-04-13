# Sentiment Analysis API

A REST API that classifies the emotional tone of input text using VADER sentiment analysis.

## Setup

```bash
pip install -r requirements.txt
/Applications/Python\ 3.12/Install\ Certificates.command
python -m nltk.downloader wordnet vader_lexicon
```

## Run

```bash
uvicorn app.main:app --reload
```

## Tests

```bash
pytest tests/ -v
```

## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/analyse` | Classify sentiment of submitted text |
| GET | `/stats` | Return average sentiment scores across all requests |

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
└── README.md
```