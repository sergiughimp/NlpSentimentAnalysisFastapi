from dataclasses import dataclass, field

@dataclass
class RequestStore:
    total_requests: int = 0
    score_total: float = 0.0
    label_counts: dict[str, int] = field(default_factory=lambda: {
        "positive": 0,
        "negative": 0,
        "neutral": 0,
    })

    def record(self, label: str, score: float) -> None:
        self.total_requests += 1
        self.score_total += score
        self.label_counts[label] += 1

    def average_score(self) -> float:
        if self.total_requests == 0:
            return 0.0
        return round(self.score_total / self.total_requests, 4)

store = RequestStore()