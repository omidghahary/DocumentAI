from chunk_selection.base_chunk_selector import BaseChunkSelector
from models.scored_chunk_model import ScoredChunkModel
from models.chunk_model import ChunkModel

class TopScoreChunkSelector(BaseChunkSelector):

    def __init__(self, max_chunks: int = 5, min_score: float = 0.0,):
        self._max_chunks = max_chunks
        self._min_score = min_score

    def select(self, scored_chunks: list[ScoredChunkModel]) -> list[ScoredChunkModel]:
        filtered = [item for item in scored_chunks if item.score >= self._min_score]
        selected = sorted(
            filtered,
            key=lambda item: item.score,
            reverse=True,
        )
        return selected[:self._max_chunks]

