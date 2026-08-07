import pytest

from chunk_scorers.base_chunk_scorer import BaseChunkScorer


def test_base_chunk_scorer_is_abstract():
    with pytest.raises(TypeError):
        BaseChunkScorer()