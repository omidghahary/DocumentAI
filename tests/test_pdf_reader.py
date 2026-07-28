
import pytest
from core.pdf_reader import PDFReader
from models.document_model import DocumentModel
from models.page_model import PageModel

@pytest.fixture
def pdf_reader():
    return PDFReader()

def test_read_single_page_pdf(pdf_reader: PDFReader, sample_pdf_single_page):

    result = pdf_reader.read(sample_pdf_single_page)
    assert isinstance(result, DocumentModel)
    assert result.page_count == 1
    assert len(result.pages) == 1

    page = result.pages[0]
    assert isinstance(page, PageModel)
    assert page.page_number == 1
    # pypdf currently extracts Persian RTL text in reverse order.
    assert "مالس" in page.text

def test_read_two_pages_pdf(pdf_reader: PDFReader, sample_pdf_two_pages):

    result = pdf_reader.read(sample_pdf_two_pages)
    assert result.page_count == 2
    assert result.pages[0].page_number == 1
    assert result.pages[1].page_number == 2
    assert "Page One" in result.pages[0].text
    assert "Page Two" in result.pages[1].text

def test_read_empty_page(pdf_reader: PDFReader, sample_pdf_empty_page):

    result = pdf_reader.read(sample_pdf_empty_page)
    assert result.page_count == 1
    assert len(result.pages) == 1

    page = result.pages[0]
    assert page.page_number == 1
    assert page.text == ""

def test_output_structure(pdf_reader: PDFReader, sample_pdf):

    result = pdf_reader.read(sample_pdf)
    assert isinstance(result, DocumentModel)
    assert isinstance(result.page_count, int)
    assert isinstance(result.pages, list)
    assert result.file_name == sample_pdf.name
    assert result.file_path == str(sample_pdf.parent)

    page = result.pages[0]
    assert isinstance(page, PageModel)
    assert isinstance(page.page_number, int)
    assert isinstance(page.text, str)
    assert page.images == []
    assert page.tables == []
    assert page.metadata == {}