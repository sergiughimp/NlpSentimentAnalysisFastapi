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
