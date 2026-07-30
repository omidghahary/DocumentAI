import pytest
from dataclasses import FrozenInstanceError
from models.llm_response_model import LLMResponseModel

def test_llm_response_model_can_be_created():
    response = LLMResponseModel(
        text="Hello",
        prompt_tokens=10,
        completion_tokens=5,
        model="mock"
    )
    assert response is not None

def test_llm_response_model_fields():
    response = LLMResponseModel(
        text="Hello",
        prompt_tokens=10,
        completion_tokens=5,
        model="mock"
    )
    assert response.text == "Hello"
    assert response.prompt_tokens == 10
    assert response.completion_tokens == 5
    assert response.model == "mock"


def test_llm_response_model_is_immutable():
    response = LLMResponseModel(
        text="Hello"
    )
    with pytest.raises(FrozenInstanceError):
        response.text = "New Text"