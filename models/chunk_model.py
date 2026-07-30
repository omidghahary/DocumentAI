from dataclasses import dataclass

@dataclass
class ChunkModel:
    chunk_id: int
    text: str
    page_numbers: list[int]
    metadata: dict