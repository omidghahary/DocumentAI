from abc import ABC, abstractmethod
from models.document_model import DocumentModel
from models.chunk_model import ChunkModel

class BaseChunker(ABC):

    @abstractmethod
    def chunk(self, document: DocumentModel) -> list[ChunkModel]:
        pass