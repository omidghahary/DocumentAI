import math
import pytest
from core.text_tokenizer import TextTokenizer
from chunk_scorers.tfidf_chunk_scorer import TfIdfChunkScorer
from models.chunk_model import ChunkModel

@pytest.fixture
def scorer():
    return TfIdfChunkScorer(TextTokenizer())

def test_tfidf_chunk_scorer_creation(scorer):
    assert scorer is not None

def test_tfidf_chunk_scorer_empty_chunks(scorer):
    scored = scorer.score([], "network")
    assert scored == []

def test_tfidf_chunk_scorer_ranks_relevant_chunk_higher(scorer):
    chunks = [
        ChunkModel(
            chunk_id=1,
            text="network configuration settings",
            page_numbers=1,
            metadata={},
        ),
        ChunkModel(
            chunk_id=2,
            text="database backup procedure",
            page_numbers=2,
            metadata={},
        ),
    ]
    scored = scorer.score(chunks, "network configuration")
    assert len(scored) == 2
    assert scored[0].score > scored[1].score

def test_tfidf_chunk_scorer_rare_term_has_higher_weight(scorer):
    chunks = [
        ChunkModel(
            chunk_id=1,
            text="network configuration",
            page_numbers=1,
            metadata={},
        ),
        ChunkModel(
            chunk_id=2,
            text="network settings",
            page_numbers=2,
            metadata={},
        ),
        ChunkModel(
            chunk_id=3,
            text="network monitoring",
            page_numbers=3,
            metadata={},
        ),
    ]
    scored = scorer.score(chunks, "network configuration")
    assert scored[0].score > scored[1].score
    assert scored[0].score > scored[2].score
    assert scored[0].score == pytest.approx(math.log(3))
    assert scored[1].score == 0.0
    assert scored[2].score == 0.0

def test_tfidf_chunk_scorer_repeated_term_behavior(scorer):
    chunks = [
        ChunkModel(
            chunk_id=1,
            text="network configuration",
            page_numbers=1,
            metadata={},
        ),
        ChunkModel(
            chunk_id=2,
            text="network network network",
            page_numbers=2,
            metadata={},
        ),
        ChunkModel(
            chunk_id=3,
            text="database backup",
            page_numbers=3,
            metadata={},
        ),
    ]
    scored = scorer.score(chunks, "network")
    assert scored[1].score > scored[0].score
    assert scored[1].score > scored[2].score

def test_tfidf_chunk_scorer_equal_term_frequency_same_score(scorer):
    chunks = [
        ChunkModel(
            chunk_id=1,
            text="network configuration",
            page_numbers=1,
            metadata={},
        ),
        ChunkModel(
            chunk_id=2,
            text="network configuration database server backup storage monitoring logging security",
            page_numbers=2,
            metadata={},
        ),
        ChunkModel(
            chunk_id=3,
            text="database backup",
            page_numbers=3,
            metadata={},
        ),
    ]
    scored = scorer.score(chunks, "network configuration")
    assert scored[0].score == pytest.approx(scored[1].score)

def test_tfidf_chunk_scorer_normalized_tf_behavior(scorer):
    chunks = [
        ChunkModel(
            chunk_id=1,
            text="configuration",
            page_numbers=1,
            metadata={},
        ),
        ChunkModel(
            chunk_id=2,
            text=(
                "configuration database server backup storage "
                "monitoring logging security authentication"
            ),
            page_numbers=2,
            metadata={},
        ),
        ChunkModel(
            chunk_id=3,
            text="database backup",
            page_numbers=3,
            metadata={},
        ),
    ]
    scored = scorer.score(chunks, "configuration")
    assert scored[0].score == pytest.approx(scored[1].score)