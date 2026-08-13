from models.document_file_type import DocumentFileType

def test_pdf_document_file_type():
    assert DocumentFileType.PDF.value == "pdf"

def test_document_file_type_is_string_enum():
    assert isinstance(DocumentFileType.PDF, str)