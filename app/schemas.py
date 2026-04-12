from pydantic import BaseModel, field_validator

class AnalyseRequest(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def text_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("text must not be empty or whitespace")
        return v

class AnalyseResponse(BaseModel):
    text: str
    label: str
    score: float

class StatsResponse(BaseModel):
    total_requests: int
    average_score: float
    label_counts: dict[str, int]