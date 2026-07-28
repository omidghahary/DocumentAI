import pytest
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

@pytest.fixture
def sample_pdf(tmp_path):
    pdf_path = tmp_path / "sample.pdf"
    pdf = canvas.Canvas(str(pdf_path))
    pdf.drawString(100, 750, "Sample PDF")
    pdf.save()
    return pdf_path

@pytest.fixture
def sample_text_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("This is a text file")
    return file_path

@pytest.fixture
def corrupted_pdf(tmp_path):
    pdf_path = tmp_path / "corrupted.pdf"
    pdf_path.write_text(
        "This is not a real pdf file"
    )
    return pdf_path
    
@pytest.fixture
def sample_pdf_single_page(tmp_path):
    font_path = "E:/AI-Projects/DocumentAI/tests/resources/fonts/DejaVuSans.ttf"
    pdfmetrics.registerFont(
        TTFont("DejaVuSans", font_path)
    )
    pdf_path = tmp_path / "single_page.pdf"
    pdf = canvas.Canvas(str(pdf_path))
    pdf.setFont("DejaVuSans", 14)
    pdf.drawString(100, 750, "سلام")
    pdf.save()
    return pdf_path

@pytest.fixture
def sample_pdf_two_pages(tmp_path):
    pdf_path = tmp_path / "two_pages.pdf"
    pdf = canvas.Canvas(str(pdf_path))
    pdf.drawString(100, 750, "Page One")
    pdf.showPage()
    pdf.drawString(100, 750, "Page Two")
    pdf.save()
    return pdf_path

@pytest.fixture
def sample_pdf_empty_page(tmp_path):
    pdf_path = tmp_path / "empty_page.pdf"
    pdf = canvas.Canvas(str(pdf_path))
    pdf.showPage()
    pdf.save()
    return pdf_path