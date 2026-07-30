from abc import ABC, abstractmethod
from models.document_model import DocumentModel

class BaseDocumentOCR(ABC):

    @abstractmethod
    def extract_document_text(self, document: DocumentModel) -> DocumentModel:
        pass