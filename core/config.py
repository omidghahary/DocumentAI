from dataclasses import dataclass

@dataclass(frozen=True)
class OCRConfig:
    tesseract_path: str = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    language: str = "fas+eng"