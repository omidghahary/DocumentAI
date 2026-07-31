import pytest
from core.config import LLMConfig
from llm.ollama_llm import OllamaLLM

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