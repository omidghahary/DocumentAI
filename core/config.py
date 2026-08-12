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
    chunk_scorer: str = "simple"
    chunk_selector: str = "simple"
    max_chunks: int = 5
    min_score: float = 0.0