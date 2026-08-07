from chunk_selection.base_chunk_selector import BaseChunkSelector
from models.scored_chunk_model import ScoredChunkModel
from models.chunk_model import ChunkModel

class TopScoreChunkSelector(BaseChunkSelector):

    def __init__(self, max_chunks: int = 5):
        self._max_chunks = max_chunks

    def select(self, scored_chunks: list[ScoredChunkModel]) -> list[ChunkModel]:
        return sorted(
            scored_chunks,
            key=lambda item:item.score,
            reverse=True
        )[:self._max_chunks]
    