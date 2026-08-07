from abc import ABC, abstractmethod
from models.chunk_model import ChunkModel

class BaseChunkSelector(ABC):

    @abstractmethod
    def select(self, chunks: list[ChunkModel]) -> list[ChunkModel]:
        pass