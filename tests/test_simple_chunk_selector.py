

import pytest
from chunk_selection.base_chunk_selector import BaseChunkSelector
from chunk_selection.simple_chunk_selector import SimpleChunkSelector
from models.chunk_model import ChunkModel

@pytest.fixture
def selector():
    return SimpleChunkSelector()

def test_simple_chunk_selector_create(selector):
    assert selector is not None

def test_simple_chunk_selector_returns_all_chunks(selector):
    chunks = [
        ChunkModel(
            chunk_id=i, 
            text= f"text {i}.",
            page_numbers=[i],
            metadata={}
            ) 
        for i in (1, 2, 3)
        ]
    selected_chunks = selector.select(chunks)
    assert selected_chunks == chunks


