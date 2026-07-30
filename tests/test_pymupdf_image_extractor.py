import pytest
import numpy as np
from images.base_image_extractor import BaseImageExtractor
from images.pymupdf_image_extractor import PyMuPDFImageExtractor
from core.pdf_reader import PDFReader

@pytest.fixture
def extractor():
    return PyMuPDFImageExtractor()

def test_pymupdf_image_extractor_can_be_instantiated(extractor):
    assert extractor is not None

def test_pymupdf_image_extractor_is_base_image_extractor(extractor):
    assert isinstance(extractor, BaseImageExtractor)

def test_extract_images_populates_page_images(extractor, sample_pdf):
    reader = PDFReader()
    document = reader.read(sample_pdf)
    document = extractor.extract_images(document)

    assert len(document.pages[0].images) == 1
    assert isinstance(document.pages[0].images[0], np.ndarray)
    assert document.pages[0].images[0].ndim == 3
    assert document.pages[0].images[0].shape[2] in [3,4]