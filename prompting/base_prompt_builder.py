from abc import ABC, abstractmethod
from models.chunk_model import ChunkModel

class BasePromptBuilder(ABC):

    @abstractmethod
    def build(self, chunk: ChunkModel) -> list[dict]:
        pass