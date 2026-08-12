from chunk_scorers.keyword_chunk_scorer import KeywordChunkScorer
from chunk_selection.top_score_chunk_selector import TopScoreChunkSelector
from models.chunk_model import ChunkModel
from core.text_tokenizer import TextTokenizer
from chunk_scorers.tfidf_chunk_scorer import TfIdfChunkScorer

def test_keyword_scorer_with_top_score_selector():
    chunks = [
        ChunkModel(
            chunk_id=1,
            text="database backup procedure",
            page_numbers=1,
            metadata={}
        ),
        ChunkModel(
            chunk_id=2,
            text="network configuration settings",
            page_numbers=2,
            metadata={}
        ),
        ChunkModel(
            chunk_id=3,
            text="network timeout configuration",
            page_numbers=3,
            metadata={}
        ),
    ]
    scorer = KeywordChunkScorer(TextTokenizer())
    selector = TopScoreChunkSelector()
    scored_chunks = scorer.score(chunks, "network configuration")
    selected_chunks = selector.select(scored_chunks)
    assert selected_chunks[0].chunk == chunks[1]
    assert selected_chunks[1].chunk == chunks[2]
    assert selected_chunks[2].chunk == chunks[0]
    assert selected_chunks[0].score == 2
    assert selected_chunks[1].score == 2
    assert selected_chunks[2].score == 0

def test_tfidf_scorer_with_top_score_selector():
    chunks = [
        ChunkModel(
            chunk_id=1,
            text="network configuration",
            page_numbers=1,
            metadata={},
        ),
        ChunkModel(
            chunk_id=2,
            text="network network network configuration",
            page_numbers=2,
            metadata={},
        ),
        ChunkModel(
            chunk_id=3,
            text="network monitoring",
            page_numbers=3,
            metadata={},
        ),
        ChunkModel(
            chunk_id=4,
            text="database backup",
            page_numbers=4,
            metadata={},
        ),
    ]
    scorer = TfIdfChunkScorer(TextTokenizer())
    scored_chunks = scorer.score(
        chunks,
        "network configuration",
    )
    selector = TopScoreChunkSelector(max_chunks=2)
    selected_chunks = selector.select(scored_chunks)
    assert len(selected_chunks) == 2
    assert selected_chunks[0].chunk.chunk_id == 2
    assert selected_chunks[1].chunk.chunk_id == 1

def test_keyword_scorer_with_threshold_selector():
    chunks = [
        ChunkModel(
            chunk_id=1,
            text="network configuration settings",
            page_numbers=1,
            metadata={}
        ),
        ChunkModel(
            chunk_id=2,
            text="network timeout",
            page_numbers=2,
            metadata={}
        ),
        ChunkModel(
            chunk_id=3,
            text="database backup procedure",
            page_numbers=3,
            metadata={}
        ),
    ]
    scorer = KeywordChunkScorer(TextTokenizer())
    selector = TopScoreChunkSelector(
        max_chunks=3,
        min_score=2,
    )
    scored_chunks = scorer.score(chunks, "network configuration")
    selected_chunks = selector.select(scored_chunks)
    assert len(selected_chunks) == 1
    assert selected_chunks[0].chunk == chunks[0]
    assert selected_chunks[0].score == 2

def test_keyword_scorer_with_threshold_and_max_chunks():
    chunks = [
        ChunkModel(
            chunk_id=1,
            text="network configuration timeout",
            page_numbers=1,
            metadata={}
        ),
        ChunkModel(
            chunk_id=2,
            text="network configuration",
            page_numbers=2,
            metadata={}
        ),
        ChunkModel(
            chunk_id=3,
            text="network settings",
            page_numbers=3,
            metadata={}
        ),
        ChunkModel(
            chunk_id=4,
            text="database backup",
            page_numbers=4,
            metadata={}
        ),
    ]
    scorer = KeywordChunkScorer(TextTokenizer())
    selector = TopScoreChunkSelector(
        max_chunks=2,
        min_score=2,
    )
    scored_chunks = scorer.score(chunks, "network configuration")
    selected_chunks = selector.select(scored_chunks)
    assert len(selected_chunks) == 2
    assert selected_chunks[0].chunk == chunks[0]
    assert selected_chunks[1].chunk == chunks[1]
    assert selected_chunks[0].score == 2
    assert selected_chunks[1].score == 2

def test_tfidf_scorer_with_top_score_selector():
    chunks = [
        ChunkModel(
            chunk_id=1,
            text="database backup procedure",
            page_numbers=1,
            metadata={}
        ),
        ChunkModel(
            chunk_id=2,
            text="network configuration settings",
            page_numbers=2,
            metadata={}
        ),
        ChunkModel(
            chunk_id=3,
            text="network configuration timeout troubleshooting",
            page_numbers=3,
            metadata={}
        ),
    ]
    scorer = TfIdfChunkScorer(TextTokenizer())
    selector = TopScoreChunkSelector(
        max_chunks=1,
        min_score=0.0,
    )
    scored_chunks = scorer.score(chunks, "network configuration timeout")
    selected_chunks = selector.select(scored_chunks)
    assert len(selected_chunks) == 1
    assert selected_chunks[0].chunk == chunks[2]