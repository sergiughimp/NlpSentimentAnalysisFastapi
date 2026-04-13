from pathlib import Path
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.main import app
from app.store import store
from model.predict import predict

client = TestClient(app)


def setup_function() -> None:
    store.total_requests = 0
    store.score_total = 0.0
    store.label_counts = {"positive": 0, "negative": 0, "neutral": 0}


def test_predict_returns_expected_shape() -> None:
    result = predict("I love how fast and helpful this service is.")
    assert set(result.keys()) == {"label", "score"}
    assert result["label"] in {"positive", "negative", "neutral"}
    assert isinstance(result["score"], float)


def test_predict_rejects_blank_text() -> None:
    try:
        predict("   ")
        assert False, "predict should fail for blank text"
    except ValueError as exc:
        assert "must not be empty" in str(exc)


def test_analyse_endpoint_returns_sentiment_payload() -> None:
    response = client.post("/analyse", json={"text": "This was okay, nothing special."})
    assert response.status_code == 200

    body = response.json()
    assert body["text"] == "This was okay, nothing special."
    assert body["label"] in {"positive", "negative", "neutral"}
    assert isinstance(body["score"], float)


def test_analyse_rejects_whitespace_only_input() -> None:
    response = client.post("/analyse", json={"text": "   "})
    assert response.status_code == 422


def test_stats_aggregation_tracks_requests_and_labels() -> None:
    texts = ["I love this", "I hate this", "It is a chair"]
    for text in texts:
        result = client.post("/analyse", json={"text": text})
        assert result.status_code == 200

    stats = client.get("/stats")
    assert stats.status_code == 200

    payload = stats.json()
    assert payload["total_requests"] == 3
    assert sum(payload["label_counts"].values()) == 3
    assert isinstance(payload["average_score"], float)