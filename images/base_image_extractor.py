from abc import ABC, abstractmethod
from models.document_model import DocumentModel


class BaseImageExtractor(ABC):

    @abstractmethod
    def extract_images(self, document: DocumentModel) -> DocumentModel:
        """
        Extract images from every page and populate page.images.
        """
        pass