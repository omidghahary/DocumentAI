from models.chunk_model import ChunkModel
from models.scored_chunk_model import ScoredChunkModel

def test_scored_chunk_model():
    chunk = ChunkModel(
        chunk_id=1,
        text="Hello World",
        page_numbers=1,
        metadata={}
    )
    scored = ScoredChunkModel(
        chunk=chunk,
        score=0.85,
    )
    assert scored.chunk == chunk
    assert scored.score == 0.85
