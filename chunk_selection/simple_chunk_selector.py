from models.chunk_model import ChunkModel
from chunk_selection.base_chunk_selector import BaseChunkSelector

class SimpleChunkSelector(BaseChunkSelector):

    def select(self, chunks: list[ChunkModel]) -> list[ChunkModel]:
        result = []
        for chunk in chunks:
            result.append(chunk)
        return result