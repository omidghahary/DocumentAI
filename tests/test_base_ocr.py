import pytest
import numpy as np
from ocr.base_ocr import BaseOCR

def test_base_ocr_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseOCR()

def test_child_without_implementation_cannot_be_instantiated():
    class DummyOCR(BaseOCR):
        pass

    with pytest.raises(TypeError):
        DummyOCR()

def test_child_with_implementation_can_be_instantiated():
    class DummyOCR(BaseOCR):
        def extract_text(self, image: np.ndarray) -> str:
            return "test text"
    ocr = DummyOCR()
    assert isinstance(ocr, BaseOCR)
    assert ocr.extract_text(np.zeros((10, 10))) == "test text"