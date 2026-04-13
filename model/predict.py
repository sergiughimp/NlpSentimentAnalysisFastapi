from __future__ import annotations

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

_analyzer: SentimentIntensityAnalyzer | None = None


def _get_analyzer() -> SentimentIntensityAnalyzer:
    global _analyzer
    if _analyzer is None:
        try:
            _analyzer = SentimentIntensityAnalyzer()
        except LookupError:
            nltk.download("vader_lexicon", quiet=True)
            _analyzer = SentimentIntensityAnalyzer()
    return _analyzer


def _label_from_compound(compound: float) -> str:
    if compound >= 0.05:
        return "positive"
    if compound <= -0.05:
        return "negative"
    return "neutral"


def predict(text: str) -> dict[str, str | float]:
    """Predict sentiment label and score for a text input."""
    cleaned_text = text.strip()
    if not cleaned_text:
        raise ValueError("text must not be empty or whitespace")

    analyzer = _get_analyzer()
    score = analyzer.polarity_scores(cleaned_text)["compound"]
    return {"label": _label_from_compound(score), "score": round(score, 4)}