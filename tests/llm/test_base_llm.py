import pytest
from llm.base_llm import BaseLLM

def test_base_llm_is_abstract():
    with pytest.raises(TypeError):
        BaseLLM()

def test_generate_method_is_required():
    class DummyLLM(BaseLLM):
        pass
    with pytest.raises(TypeError):
        DummyLLM()