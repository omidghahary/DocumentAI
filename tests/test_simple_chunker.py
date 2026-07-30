from chunking.simple_chunker import SimpleChunker
from models.document_model import DocumentModel
from models.page_model import PageModel

def test_simple_chunker_can_be_instantiated():
    chunker = SimpleChunker()
    assert chunker is not None

def test_simple_chunker_chunks_eq_pages():
    chunker = SimpleChunker()
    page = PageModel(
        page_number=1,
        text="page 1",
        images=[]
    )
    document = DocumentModel(
        file_name="test.pdf",
        file_path="doc/",
        page_count=1,
        pages=[page]
    )
    chunks = chunker.chunk(document)
    assert len(chunks) == len(document.pages)
    assert chunks[0].page_numbers == [1]
    assert chunks[0].text == document.pages[0].text

def test_simple_chunker_multiple_pages():
    chunker = SimpleChunker()
    pages = [
        PageModel(
            page_number=1,
            text="page one",
            images=[]
        ),
        PageModel(
            page_number=2,
            text="page two",
            images=[]
        )
    ]
    document = DocumentModel(
        file_name="test.pdf",
        file_path="doc/",
        page_count=2,
        pages=pages
    )
    chunks = chunker.chunk(document)
    assert len(chunks) == 2
    assert chunks[0].page_numbers == [1]
    assert chunks[1].page_numbers == [2]
    assert chunks[0].text == "page one"
    assert chunks[1].text == "page two"