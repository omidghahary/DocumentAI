from llm.base_llm import BaseLLM
from models.llm_response_model import LLMResponseModel

class MockLLM(BaseLLM):
    def generate(self, messages: list[dict]) -> LLMResponseModel:
        return LLMResponseModel(
            text="Mock Response",
            prompt_tokens=10,
            completion_tokens=5,
            model="mock"
            )