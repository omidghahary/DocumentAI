import pytest
from ocr.base_document_ocr import BaseDocumentOCR

def test_base_document_ocr_is_abstract():
    with pytest.raises(TypeError):
        BaseDocumentOCR()

def test_extract_document_text_is_required():
    class DummyDocumentOCR(BaseDocumentOCR):
        pass
    with pytest.raises(TypeError):
        DummyDocumentOCR()