from chunk_scorers.keyword_chunk_scorer import KeywordChunkScorer
from chunk_selection.top_score_chunk_selector import TopScoreChunkSelector
from models.chunk_model import ChunkModel

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
    scorer = KeywordChunkScorer()
    selector = TopScoreChunkSelector()
    scored_chunks = scorer.score(chunks, "network configuration")
    selected_chunks = selector.select(scored_chunks)
    assert selected_chunks[0].chunk == chunks[1]
    assert selected_chunks[1].chunk == chunks[2]
    assert selected_chunks[2].chunk == chunks[0]
    assert selected_chunks[0].score == 2
    assert selected_chunks[1].score == 2
    assert selected_chunks[2].score == 0