from pathlib import Path
from pypdf import PdfReader
from models.document_model import DocumentModel
from models.page_model import PageModel

class PDFReader:
    def read(self, path: str | Path) -> DocumentModel:
        path = Path(path)
        pdf = PdfReader(str(path))
        document_model = DocumentModel(
            file_name = path.name,
            file_path = str(path.parent),
            page_count = len(pdf.pages)
        )
        for index, page in enumerate(pdf.pages):
            document_model.pages.append(
                PageModel(
                    page_number = index + 1,
                    text = page.extract_text() or ""
                )
            )
        return document_model