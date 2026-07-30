import pytest
from chunking.base_chunker import BaseChunker

def test_base_chunker_is_abstract():
    with pytest.raises(TypeError):
        BaseChunker()

def test_chunk_method_is_required():
    class DummyChunker(BaseChunker):
        pass
    with pytest.raises(TypeError):
        DummyChunker()