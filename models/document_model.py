from dataclasses import dataclass, field
from models.page_model import PageModel

@dataclass
class DocumentModel:
    file_name: str
    file_path: str
    page_count: int
    pages: list[PageModel] = field(default_factory=list)