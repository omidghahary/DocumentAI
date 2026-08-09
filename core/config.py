from dataclasses import dataclass

@dataclass(frozen=True)
class OCRConfig:
    tesseract_path: str = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    language: str = "fas+eng"

@dataclass(frozen=True)
class LLMConfig:
    provider: str
    base_url: str
    model_name: str
    temperature: float
    timeout: int

@dataclass(frozen=True)
class RetrievalConfig:
    chunk_scorer: str = "keyword"
    chunk_selector: str = "top_score"
    max_chunks: int = 5