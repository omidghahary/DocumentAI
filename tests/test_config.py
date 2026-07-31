from dataclasses import FrozenInstanceError
import pytest
from core.config import OCRConfig
from core.config import LLMConfig

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

def test_llm_config_can_be_created():
    config = LLMConfig(
        provider="ollama",
        base_url="http://localhost:11434",
        model_name="qwen2.5:3b",
        temperature=0.1,
        timeout=120
    )
    assert config is not None

def test_llm_config_fields():
    config = LLMConfig(
        provider="ollama",
        base_url="http://localhost:11434",
        model_name="qwen2.5:3b",
        temperature=0.1,
        timeout=120
    )
    assert config.provider == "ollama"
    assert config.base_url == "http://localhost:11434"
    assert config.model_name == "qwen2.5:3b"
    assert config.temperature == 0.1
    assert config.timeout == 120

def test_llm_config_is_immutable():
    config = LLMConfig(
        provider="ollama",
        base_url="http://localhost:11434",
        model_name="qwen2.5:3b",
        temperature=0.1,
        timeout=120
    )
    with pytest.raises(FrozenInstanceError):
        config.model_name = "llama3"