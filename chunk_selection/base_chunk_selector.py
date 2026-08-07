from abc import ABC, abstractmethod
from models.chunk_model import ChunkModel
from models.scored_chunk_model import ScoredChunkModel

class BaseChunkSelector(ABC):

    @abstractmethod
    def select(self, scored_chunks: list[ScoredChunkModel]) -> list[ChunkModel]:
        pass