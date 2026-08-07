from chunk_scorers.base_chunk_scorer import BaseChunkScorer
from models.chunk_model import ChunkModel
from models.scored_chunk_model import ScoredChunkModel

class SimpleChunkScorer(BaseChunkScorer):
    """
    A basic chunk scorer that assigns the same score
    to every chunk.
    """

    def score(self, chunks: list[ChunkModel], query: str) -> list[ScoredChunkModel]:
        return [
            ScoredChunkModel(
                chunk=chunk,
                score=1.0,
            )
            for chunk in chunks
        ]