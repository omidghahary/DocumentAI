from llm.mock_llm import MockLLM
from llm.base_llm import BaseLLM
from models.llm_response_model import LLMResponseModel


def test_mock_llm_can_be_instantiated():
    llm = MockLLM()
    assert llm is not None

def test_mock_llm_is_base_llm():
    llm = MockLLM()
    assert isinstance(llm, BaseLLM)

def test_mock_llm_returns_llm_response():
    llm = MockLLM()
    messages = [
        {
            "role": "user",
            "content": "Hello"
        }
    ]
    result = llm.generate(messages)
    assert isinstance(result, LLMResponseModel)

def test_mock_llm_response_content():
    llm = MockLLM()
    result = llm.generate([])
    assert result.text == "Mock Response"
    assert result.model == "mock"