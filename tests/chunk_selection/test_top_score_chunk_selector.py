
import pytest
from chunk_selection.top_score_chunk_selector import TopScoreChunkSelector
from models.chunk_model import ChunkModel
from models.scored_chunk_model import ScoredChunkModel

@pytest.fixture
def scored_chunks():
    scored_chunk_A = ScoredChunkModel(
        chunk= ChunkModel(
            chunk_id=1,
            text="test1",
            page_numbers=1,
            metadata={},
        ),
        score=1
    )
    scored_chunk_B = ScoredChunkModel(
        chunk= ChunkModel(
            chunk_id=2,
            text="test2",
            page_numbers=2,
            metadata={},
        ),
        score=5
    )
    scored_chunk_C = ScoredChunkModel(
        chunk= ChunkModel(
            chunk_id=3,
            text="test3",
            page_numbers=3,
            metadata={},
        ),
        score=3
    )
    return [scored_chunk_A, scored_chunk_B, scored_chunk_C]

@pytest.fixture
def selector():
    return TopScoreChunkSelector()

def test_top_score_chunk_selector_create(selector):
    assert selector is not None

def test_top_score_chunk_selector_sort_3_chunk(selector, scored_chunks):
    selected_chunks = selector.select(scored_chunks)
    assert selected_chunks[0] == scored_chunks[1]
    assert selected_chunks[1] == scored_chunks[2]
    assert selected_chunks[2] == scored_chunks[0]
    
def test_top_score_chunk_selector_output_limitaion(scored_chunks):
    selector = TopScoreChunkSelector(max_chunks=2)
    selected_chunks = selector.select(scored_chunks)
    assert len(selected_chunks) == 2
    assert selected_chunks[0] == scored_chunks[1]
    assert selected_chunks[1] == scored_chunks[2]

def test_top_score_chunk_selector_empty_chunk(selector):
    selected_chunks = selector.select([])
    assert len(selected_chunks) == 0
