
import pytest
from chunk_scorers.keyword_chunk_scorer import KeywordChunkScorer
from models.chunk_model import ChunkModel

@pytest.fixture
def scorer():
    return KeywordChunkScorer()

def test_keyword_chunk_scorer_creation(scorer):
    assert scorer is not None

def test_keyword_chunk_scorer_score_computation(scorer):
    chunk1 = ChunkModel(
        chunk_id=1,
        text="network timeout configuration",
        page_numbers=1,
        metadata={},
    )
    chunk2= ChunkModel(
        chunk_id=2,
        text="network configuration",
        page_numbers=2,
        metadata={},
    )
    chunk3 = ChunkModel(
        chunk_id=3,
        text="database backup",
        page_numbers=3,
        metadata={},
    )
    
    chunks = [chunk1, chunk2, chunk3]
    scored = scorer.score(chunks, "network configuration")
    assert len(scored) == len(chunks)
    assert scored[0].score == 2
    assert scored[1].score == 2
    assert scored[2].score == 0
    assert scored[0].chunk == chunk1
    assert scored[1].chunk == chunk2
    assert scored[2].chunk == chunk3

def test_keyword_chunk_scorer_empty_query(scorer):
    chunk = ChunkModel(
        chunk_id=1,
        text="network timeout configuration",
        page_numbers=1,
        metadata={},
    )
    scored = scorer.score([chunk], "")
    assert scored[0].score == 0


def test_keyword_chunk_scorer_empty_chunk(scorer):
    chunk = ChunkModel(
        chunk_id=1,
        text="",
        page_numbers=1,
        metadata={},
    )
    scored = scorer.score([chunk], "test")
    assert scored[0].score == 0


def test_keyword_chunk_scorer_punctuation(scorer):
    chunk = ChunkModel(
        chunk_id=1,
        text="network configuration settings",
        page_numbers=1,
        metadata={},
    )
    scored = scorer.score([chunk], "Network, configuration!")
    assert scored[0].score == 2

def test_keyword_chunk_scorer_case_insensitive(scorer):
    chunk = ChunkModel(
        chunk_id=1,
        text="Network Configuration",
        page_numbers=1,
        metadata={},
    )
    scored = scorer.score([chunk], "network configuration")
    assert scored[0].score == 2

def test_keyword_chunk_scorer_does_not_match_partial_word(scorer):
    chunk = ChunkModel(
        chunk_id=1,
        text="network configuration",
        page_numbers=1,
        metadata={},
    )
    scored = scorer.score([chunk], "net")
    assert scored[0].score == 0

def test_keyword_chunk_scorer_matches_complete_words(scorer):
    chunk = ChunkModel(
        chunk_id=1,
        text="network configuration",
        page_numbers=1,
        metadata={},
    )
    scored = scorer.score([chunk], "network")
    assert scored[0].score == 1

def test_keyword_chunk_scorer_normalizes_chunk_punctuation(scorer):
    chunk = ChunkModel(
        chunk_id=1,
        text="Network, configuration settings.",
        page_numbers=1,
        metadata={},
    )
    scored = scorer.score([chunk], "network configuration")
    assert scored[0].score == 2