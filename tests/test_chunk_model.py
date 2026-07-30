from models.chunk_model import ChunkModel

def test_chunk_model_can_be_created():
    chunk = ChunkModel(
        chunk_id=1,
        text="This is a test chunk",
        page_numbers=[1, 2],
        metadata={}
    )
    assert chunk is not None


def test_chunk_model_fields():
    chunk = ChunkModel(
        chunk_id=1,
        text="Sample text",
        page_numbers=[3],
        metadata={
            "source": "test"
        }
    )

    assert chunk.chunk_id == 1
    assert chunk.text == "Sample text"
    assert chunk.page_numbers == [3]
    assert chunk.metadata["source"] == "test"