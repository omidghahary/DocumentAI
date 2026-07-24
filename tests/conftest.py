import pytest
from reportlab.pdfgen import canvas

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