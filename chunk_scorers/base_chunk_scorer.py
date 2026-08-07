from abc import ABC, abstractmethod
from models.chunk_model import ChunkModel
from models.scored_chunk_model import ScoredChunkModel

class BaseChunkScorer(ABC):
    """
    Base interface for scoring document chunks according to
    their relevance to a query.
    """

    @abstractmethod
    def score(
        self,
        chunks: list[ChunkModel],
        query: str,
    ) -> list[ScoredChunkModel]:
        """
        Score the given chunks.

        Args:
            chunks: Document chunks.
            query: User query.

        Returns:
            A list of scored chunks.
        """
        raise NotImplementedError