import pytest
import numpy as np
from ocr.base_ocr import BaseOCR
from ocr.tesseract_ocr import TesseractOCR
from core.config import OCRConfig

@pytest.fixture
def ocr_config():
    return OCRConfig

@pytest.fixture
def tesseract_ocr(ocr_config):
    return TesseractOCR(ocr_config)

def test_tesseract_ocr_can_be_instantiated(tesseract_ocr):
    assert tesseract_ocr is not None

def test_tesseract_ocr_is_base_ocr(tesseract_ocr):
    assert isinstance(tesseract_ocr, BaseOCR)

def test_tesseract_ocr_extract_text(tesseract_ocr, ocr_test_image):
    result = tesseract_ocr.extract_text(ocr_test_image)
    assert "Hello" in result

def test_tesseract_ocr_invalid_input(tesseract_ocr):
    with pytest.raises(TypeError):
        tesseract_ocr.extract_text("image.jpg")