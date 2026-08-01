from dataclasses import dataclass

@dataclass(frozen=True)
class ContextModel:
    text: str
    source_chunks: list[int]
    token_count: int = 0