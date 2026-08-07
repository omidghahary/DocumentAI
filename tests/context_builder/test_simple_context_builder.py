import pytest
from context.simple_context_builder import SimpleContextBuilder
from models.chunk_model import ChunkModel


@pytest.fixture
def builder():
    return SimpleContextBuilder()

def test_simple_context_builder_create(builder):
    assert builder is not None

def test_simple_context_builder_3_chunk_to_context(builder):
    chunks = [
        ChunkModel(
            chunk_id= i,
            text= f"chunk {i},",
            page_numbers= i,
            metadata={
                "source": "PDF 1"
            }
        ) 
        for i in (1, 2, 3)
        ]
    context = builder.build(chunks)
    assert context.token_count == 0
    assert context.source_chunks == [1, 2, 3]
    assert "chunk 2" in context.text
    assert context.text == ("chunk 1,\n\nchunk 2,\n\nchunk 3,")