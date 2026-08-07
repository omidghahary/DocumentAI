import pytest
from core.config import LLMConfig
from llm.ollama_llm import OllamaLLM
from unittest.mock import Mock, patch
from models.llm_response_model import LLMResponseModel

@pytest.fixture
def llm_config():
    return LLMConfig(
        provider="ollama",
        base_url="http://localhost:11434",
        model_name="qwen2.5:3b",
        temperature=0.1,
        timeout=120
    )

@pytest.fixture
def ollama_llm(llm_config):
    return OllamaLLM(llm_config)

def test_ollama_llm_is_used_config(ollama_llm, llm_config):
    assert ollama_llm.config is llm_config

def test_ollama_llm_build_payload(ollama_llm):
    messages = [
        {
            "role": "user",
            "content": "OCR چیست؟"
        }
    ]
    payload = ollama_llm._build_payload(messages)
    assert payload["model"] == "qwen2.5:3b"
    assert payload["messages"] == messages
    assert payload["stream"] is False

def test_ollama_llm_send_request(ollama_llm):
    payload = {
        "model": "qwen2.5:3b",
        "messages": [
            {
                "role": "user",
                "content": "hello"
            }
        ],
        "stream": False
    }
    fake_response = Mock()
    with patch("requests.post", return_value=fake_response) as mock_post:
        result = ollama_llm._send_request(payload)

    mock_post.assert_called_once_with(
        "http://localhost:11434/api/chat",
        json=payload,
        timeout=120
    )

    assert result is fake_response

def test_ollama_llm_parse_response(ollama_llm):

    fake_response = Mock()
    fake_response.json.return_value = {
        "model": "qwen2.5:3b",
        "message": {
            "role": "assistant",
            "content": "OCR is a technology for text recognition."
        },
        "prompt_eval_count": 25,
        "eval_count": 40
    }
    result = ollama_llm._parse_response(fake_response)
    assert isinstance(result, LLMResponseModel)
    assert result.text == "OCR is a technology for text recognition."
    assert result.prompt_tokens == 25
    assert result.completion_tokens == 40
    assert result.model == "qwen2.5:3b"