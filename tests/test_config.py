import pytest
from core.config import OCRConfig

def test_ocr_config_can_be_created():
    config = OCRConfig(
        tesseract_path="C:/Program Files/Tesseract-OCR/tesseract.exe"
    )
    assert config.tesseract_path == "C:/Program Files/Tesseract-OCR/tesseract.exe"

def test_ocr_config_default_language():
    config = OCRConfig(
        tesseract_path="C:/Program Files/Tesseract-OCR/tesseract.exe"
    )
    assert config.language == "fas+eng"

def test_ocr_config_is_immutable():
    config = OCRConfig(
        tesseract_path="C:/Program Files/Tesseract-OCR/tesseract.exe"
    )
    with pytest.raises(AttributeError):
        config.language = "fas"