from abc import ABC, abstractmethod
from models.chunk_model import ChunkModel
from models.context_model import ContextModel

class BaseContextBuilder(ABC):
    
    @abstractmethod
    def build(self, chunks: list[ChunkModel]) -> ContextModel:
        """
        Build an optimized context from document chunks.
        """
        raise NotImplementedError