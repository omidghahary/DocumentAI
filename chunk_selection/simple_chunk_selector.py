from models.chunk_model import ChunkModel
from chunk_selection.base_chunk_selector import BaseChunkSelector
from models.scored_chunk_model import ScoredChunkModel

class SimpleChunkSelector(BaseChunkSelector):

    def select(self, scored_chunks: list[ScoredChunkModel])  -> list[ChunkModel]:
        return [
            scored.chunk
            for scored in scored_chunks
        ]