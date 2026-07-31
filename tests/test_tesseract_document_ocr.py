
import pytest
from ocr.base_document_ocr import BaseDocumentOCR
from ocr.tesseract_document_ocr import TesseractDocumentOCR
from core.config import OCRConfig
from ocr.tesseract_ocr import TesseractOCR
from ocr.base_ocr import BaseOCR
from core.pdf_reader import PDFReader
from models.document_model import DocumentModel
from models.page_model import PageModel
from images.pymupdf_image_extractor import PyMuPDFImageExtractor

@pytest.fixture
def ocr_config():
    return OCRConfig

@pytest.fixture
def ocr_engine(ocr_config):
    return TesseractOCR(ocr_config)

@pytest.fixture
def processor(ocr_engine):
    return TesseractDocumentOCR(ocr_engine)

def test_tesseract_document_ocr_can_be_instantiated(processor):
    assert processor is not None

def test_tesseract_document_ocr_is_base_document_ocr(processor):
    assert isinstance(processor, BaseDocumentOCR)

def test_tesseract_document_ocr_hold_ocr_engine(processor, ocr_engine):
    assert isinstance(processor.ocr_engine, BaseOCR)
    assert processor.ocr_engine is ocr_engine

def test_tesseract_document_ocr_run_method_without_err(processor, sample_pdf):
    reader = PDFReader()
    document = reader.read(sample_pdf)
    extractor = PyMuPDFImageExtractor()
    document = extractor.extract_images(document)
    result = processor.extract_document_text(document)
    assert result is document

def test_tesseract_document_ocr_empty_page(processor):
    page = PageModel(
        page_number=1,
        text="",
        images=[]
    )
    document = DocumentModel(
        file_name="test.pdf",
        file_path="doc/",
        page_count=1,
        pages=[page]
    )
    with pytest.raises(
        ValueError,
        match="has no extracted image",
        ):
        processor.extract_document_text(document)

def test_tesseract_document_ocr_full_pipline(processor, sample_pdf):
    reader = PDFReader()
    document = reader.read(sample_pdf)
    extractor = PyMuPDFImageExtractor()
    document = extractor.extract_images(document)
    result = processor.extract_document_text(document)
    assert isinstance(result.pages[0].text, str)
    assert result.pages[0].text != ""
    assert "Sample PDF" in result.pages[0].text
    