import fitz
import numpy as np
from images.base_image_extractor import BaseImageExtractor
from models.document_model import DocumentModel

class PyMuPDFImageExtractor(BaseImageExtractor):

    def __init__(self):
        pass

    def extract_images(self, document: DocumentModel) -> DocumentModel:
        pdf_path = document.file_path + "/" + document.file_name
        pdf_doc = fitz.open(str(pdf_path))
        if len(pdf_doc) != len(document.pages):
            raise ValueError("PDF page count and document model page count are inconsistent")
        for page_model, page in zip(document.pages, pdf_doc):
            pix = page.get_pixmap()
            image = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
            page_model.images.append(image)

        return document