import string
from chunk_scorers.base_chunk_scorer import BaseChunkScorer
from models.chunk_model import ChunkModel
from models.scored_chunk_model import ScoredChunkModel
from core.text_tokenizer import TextTokenizer

class KeywordChunkScorer(BaseChunkScorer):
    """
    Scores chunks based on keyword occurrence in text.
    """

    def __init__(self, tokenizer: TextTokenizer):
        self._tokenizer = tokenizer
        
    def score(self, chunks: list[ChunkModel], query: str) -> list[ScoredChunkModel]:
        keywords = set(self._tokenizer.tokenize(query))
        scored_chunks = []
        for chunk in chunks:
            text = set(self._tokenizer.tokenize(chunk.text))
            score = sum(1 for keyword in keywords if keyword in text)
            scored_chunks.append(
                ScoredChunkModel(chunk=chunk, score=float(score))
            )
        return scored_chunks