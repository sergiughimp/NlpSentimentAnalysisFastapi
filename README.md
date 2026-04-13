# Sentiment Analysis API

A REST API that classifies the emotional tone of input text using VADER sentiment analysis.

## Setup

```bash
pip install -r requirements.txt
python -m nltk.downloader vader_lexicon
```

## Run

```bash
uvicorn app.main:app --reload
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