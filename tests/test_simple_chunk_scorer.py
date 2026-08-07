
import pytest

from models.chunk_model import ChunkModel
from models.scored_chunk_model import ScoredChunkModel
from chunk_scorers.simple_chunk_scorer import SimpleChunkScorer

@pytest.fixture
def scorer():
    return SimpleChunkScorer()

def test_simple_chunk_scorer_creation(scorer):
    assert scorer is not None

def test_simple_chunk_scorer_returns_all_chunks(scorer):
    chunks = [
        ChunkModel(
            chunk_id=i, 
            text= f"text {i}.",
            page_numbers=[i],
            metadata={}
            ) 
        for i in (1, 2, 3)
        ]
    scored = scorer.score(chunks, "for test")
    assert len(scored) == len(chunks)
    for scored_chunk, original_chunk in zip(scored, chunks):
        assert scored_chunk.score == 1.0
        assert scored_chunk.chunk == original_chunk
    
def test_simple_chunk_scorer_empty_chunk(scorer):
    chunks = []
    scored = scorer.score(chunks, "for test")
    assert scored == []