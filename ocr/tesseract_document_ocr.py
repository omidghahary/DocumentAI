from models.document_model import DocumentModel
from ocr.base_document_ocr import BaseDocumentOCR
from ocr.base_ocr import BaseOCR

class TesseractDocumentOCR(BaseDocumentOCR):

    def __init__(self, ocr_engine: BaseOCR):
        self.ocr_engine = ocr_engine

    def extract_document_text(self, document: DocumentModel) -> DocumentModel:
        for page in document.pages:
            if not page.images:
                raise ValueError(
                    f"Page {page.page_number} has no extracted image."
                )
            page.text = self.ocr_engine.extract_text(page.images[0])
        return document