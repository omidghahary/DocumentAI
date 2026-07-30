from dataclasses import dataclass, field

@dataclass
class PageModel:
    page_number: int
    text: str
    images: list = field(default_factory=list)
    tables: list = field(default_factory=list)
    metadata: dict = field(default_factory=dict)