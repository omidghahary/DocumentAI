import pytest
from reportlab.pdfgen import canvas
from core.pdf_reader import PDFReader

@pytest.fixture
def pdf_reader():
    return PDFReader()

def test_read_single_page_pdf(pdf_reader: PDFReader, sample_pdf_single_page):

    result = pdf_reader.read(sample_pdf_single_page)
    assert isinstance(result, dict)
    assert result["page_count"] == 1
    assert len(result["pages"]) == 1

    page = result["pages"][0]
    assert isinstance(page, dict)
    assert page["page_number"] == 1
    assert "مالس" in page["text"]

def test_read_two_pages_pdf(pdf_reader: PDFReader, sample_pdf_two_pages):

    result = pdf_reader.read(sample_pdf_two_pages)
    assert result["page_count"] == 2
    assert result["pages"][0]["page_number"] == 1
    assert result["pages"][1]["page_number"] == 2
    assert "Page One" in result["pages"][0]["text"]
    assert "Page Two" in result["pages"][1]["text"]

def test_read_empty_page(pdf_reader: PDFReader, sample_pdf_empty_page):

    result = pdf_reader.read(sample_pdf_empty_page)
    assert result["page_count"] == 1
    assert len(result["pages"]) == 1

    page = result["pages"][0]
    assert page["page_number"] == 1
    assert page["text"] == ""

def test_output_structure(pdf_reader: PDFReader, sample_pdf):

    result = pdf_reader.read(sample_pdf)
    assert isinstance(result, dict)
    assert "page_count" in result
    assert "pages" in result
    assert isinstance(result["page_count"], int)
    assert isinstance(result["pages"], list)

    page = result["pages"][0]
    assert isinstance(page, dict)
    assert "page_number" in page
    assert "text" in page
    assert isinstance(page["page_number"], int)
    assert isinstance(page["text"], str)