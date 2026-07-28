from ocr.base_ocr import BaseOCR
from core.config import OCRConfig
import pytesseract
import numpy as np

class TesseractOCR(BaseOCR):

    def __init__(self, config: OCRConfig):
        self._config = config()
        pytesseract.pytesseract.tesseract_cmd = config.tesseract_path

    def extract_text(self, image: np.ndarray) -> str:
        if not isinstance(image, np.ndarray):
            raise TypeError("image must be numpy array")
        return pytesseract.image_to_string(
            image,
            lang=self._config.language
        )