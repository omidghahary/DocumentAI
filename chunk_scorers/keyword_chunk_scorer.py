from chunk_scorers.base_chunk_scorer import BaseChunkScorer
from models.chunk_model import ChunkModel
from models.scored_chunk_model import ScoredChunkModel

class KeywordChunkScorer(BaseChunkScorer):
    """
    Scores chunks based on keyword occurrence in text.
    """
    def score(self, chunks: list[ChunkModel], query: str) -> list[ScoredChunkModel]:
        keywords = query.lower().split()
        scored_chunks = []
        for chunk in chunks:
            text = chunk.text.lower()
            score = sum(text.count(keyword) for keyword in keywords)
            scored_chunks.append(
                ScoredChunkModel(chunk=chunk, score=float(score))
            )
        return scored_chunks