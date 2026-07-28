from pathlib import Path
from pypdf import PdfReader

class PDFReader:
    def read(self, path: str | Path) -> dict:
        pdf = PdfReader(str(path))
        pages = []
        for index, page in enumerate(pdf.pages):
            text = page.extract_text()
            pages.append(
                {
                    "page_number": index + 1,
                    "text": text or ""
                }
            )
        return {
            "page_count": len(pages),
            "pages": pages
        }