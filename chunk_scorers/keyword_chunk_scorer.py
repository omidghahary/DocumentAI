import string
from chunk_scorers.base_chunk_scorer import BaseChunkScorer
from models.chunk_model import ChunkModel
from models.scored_chunk_model import ScoredChunkModel

class KeywordChunkScorer(BaseChunkScorer):
    """
    Scores chunks based on keyword occurrence in text.
    """
    def score(self, chunks: list[ChunkModel], query: str) -> list[ScoredChunkModel]:
        translator = str.maketrans('', '', string.punctuation)
        keywords = query.translate(translator).lower().split()
        scored_chunks = []
        for chunk in chunks:
            text = chunk.text.translate(translator).lower().split()
            score = sum(
                len([
                    word 
                    for word in text 
                    if word == keyword
                    ]) 
                for keyword in keywords
                )
            scored_chunks.append(
                ScoredChunkModel(chunk=chunk, score=float(score))
            )
        return scored_chunks