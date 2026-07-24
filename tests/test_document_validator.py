import pytest
from core.document_validator import DocumentValidator

@pytest.fixture
def document_validator():
    return DocumentValidator()

def test_validate_valid_pdf(document_validator, sample_pdf):
    result = document_validator.validate(sample_pdf)
    assert result is None

def test_validate_missing_file(document_validator, tmp_path):
    missing_file = tmp_path / "missing.pdf"
    with pytest.raises(FileNotFoundError):
        document_validator.validate(missing_file)

def test_validate_non_pdf_file(document_validator, sample_text_file):
    with pytest.raises(ValueError):
        document_validator.validate(sample_text_file)

def test_validate_none_input(document_validator):
    with pytest.raises(ValueError):
        document_validator.validate(None)

def test_validate_invalid_input_type(document_validator):
    with pytest.raises(TypeError):
        document_validator.validate(123)

def test_validate_corrupted_pdf(document_validator, corrupted_pdf):
    with pytest.raises(ValueError):
        document_validator.validate(corrupted_pdf)