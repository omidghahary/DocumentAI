from dataclasses import dataclass
from models.chunk_model import ChunkModel

@dataclass(frozen=True)
class ScoredChunkModel:
    """
    Represents a chunk together with its relevance score.
    """
    
    chunk: ChunkModel
    score: float