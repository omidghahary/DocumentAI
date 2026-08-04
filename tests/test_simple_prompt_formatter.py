import pytest
from models.prompt_model import PromptModel
from prompting.simple_prompt_formatter import SimplePromptFormatter

@pytest.fixture
def formatter():
    return SimplePromptFormatter()

def test_simple_prompt_formatter_can_be_created(formatter):
    assert formatter is not None

def test_simple_prompt_formatter_returns_chat_messages(formatter):

    prompt = PromptModel(text="Analyze this document.")
    messages = formatter.format(prompt)
    assert isinstance(messages, list)
    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert messages[1]["content"] == "Analyze this document."