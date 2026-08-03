import pytest
from dataclasses import FrozenInstanceError
from models.prompt_model import PromptModel

@pytest.fixture
def prompt():
    return PromptModel(text="test prompt")

def test_prompt_model_can_be_created(prompt):
    assert prompt is not None

def test_prompt_model_fields(prompt):
    assert prompt.text == "test prompt"

def test_prompt_model_is_immutable(prompt):
    with pytest.raises(FrozenInstanceError):
        prompt.text = "new prompt"