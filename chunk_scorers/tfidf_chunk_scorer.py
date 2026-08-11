import math
from chunk_scorers.base_chunk_scorer import BaseChunkScorer
from models.chunk_model import ChunkModel
from models.scored_chunk_model import ScoredChunkModel
from core.text_tokenizer import TextTokenizer

class TfIdfChunkScorer(BaseChunkScorer):

    def __init__(self, tokenizer: TextTokenizer):
        self._tokenizer = tokenizer

    def score(self, chunks: list[ChunkModel], query: str) -> list[ScoredChunkModel]:
        if not chunks:
            return []
        query_terms = set(self._tokenizer.tokenize(query))
        tokenized_chunks = [
            self._tokenizer.tokenize(chunk.text)
            for chunk in chunks
        ]
        document_frequency = {
            term: sum(
                1
                for chunk_terms in tokenized_chunks
                if term in set(chunk_terms)
            )
            for term in query_terms
        }
        total_chunks = len(chunks)
        scored_chunks = []
        for chunk, chunk_terms in zip(chunks, tokenized_chunks):
            score = 0.0
            for term in query_terms:
                tf = chunk_terms.count(term)
                df = document_frequency[term]
                idf = math.log(total_chunks / df)
                score += tf * idf
            scored_chunks.append(
                ScoredChunkModel(
                    chunk=chunk,
                    score=score
                )
            )
        return scored_chunks