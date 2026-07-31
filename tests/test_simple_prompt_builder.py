import pytest
from prompting.base_prompt_builder import BasePromptBuilder
from prompting.simple_prompt_builder import SimplePromptBuilder
from models.chunk_model import ChunkModel

@pytest.fixture
def base_builder():
    return BasePromptBuilder

@pytest.fixture
def simple_builder():
    return SimplePromptBuilder()

def test_simple_prompt_builder_can_be_instantiated(simple_builder):
    assert simple_builder is not None

def test_simple_prompt_builder_returns_messages(simple_builder):
    chunk = ChunkModel(
        chunk_id=1,
        text="This is a test document",
        page_numbers=[1],
        metadata={}
    )
    messages = simple_builder.build(chunk)
    assert isinstance(messages, list)
    assert len(messages) == 2

def test_simple_prompt_builder_message_roles(simple_builder):

    chunk = ChunkModel(
        chunk_id=1,
        text="Hello",
        page_numbers=[1],
        metadata={}
    )
    messages = simple_builder.build(chunk)
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"