import pytest
from chunk_selection.simple_chunk_selector import SimpleChunkSelector
from models.chunk_model import ChunkModel
from models.scored_chunk_model import ScoredChunkModel

@pytest.fixture
def selector():
    return SimpleChunkSelector()

def test_simple_chunk_selector_create(selector):
    assert selector is not None

def test_simple_chunk_selector_returns_all_chunks(selector):
    chunks = [
        ChunkModel(
            chunk_id=i,
            text=f"text {i}.",
            page_numbers=[i],
            metadata={}
        )
        for i in (1,2,3)
    ]
    scored_chunks = [
        ScoredChunkModel(
            chunk=chunk,
            score=1.0
        )
        for chunk in chunks
    ]
    selected_chunks = selector.select(scored_chunks)
    assert selected_chunks == chunks


