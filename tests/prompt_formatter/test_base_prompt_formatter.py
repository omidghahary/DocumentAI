import pytest
from models.prompt_model import PromptModel
from prompting.base_prompt_formatter import BasePromptFormatter

class FakePromptFormatter(BasePromptFormatter):

    def format(self, prompt: PromptModel) -> list[dict]:
        return [
            {
                "role": "user",
                "content": prompt.text
            }
        ]

@pytest.fixture
def formatter():
    return FakePromptFormatter()

def test_base_prompt_formatter_can_be_created(formatter):
    assert formatter is not None

def test_base_prompt_formatter_returns_messages(formatter):
    prompt = PromptModel(text="Hello World")
    messages = formatter.format(prompt)

    assert isinstance(messages, list)
    assert messages[0]["role"] == "user"
    assert messages[0]["content"] == "Hello World"