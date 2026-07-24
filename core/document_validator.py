from pathlib import Path
from pypdf import PdfReader

class DocumentValidator:

    def validate(self, path):

        if path is None:
            raise ValueError("Input must not be None.")

        if not isinstance(path, (Path, str)):
            raise TypeError("input must str or path object.")

        if isinstance(path, str):
            path = Path(path)

        if not path.exists():
            raise FileNotFoundError(f"file not found: {path}")

        if path.suffix.lower() != ".pdf":
            raise ValueError(f"file type is not PDF: {path}")

        try:
            PdfReader(str(path))
        except Exception as e:
            raise ValueError("pdf file is corrupted.") from e
        return None

