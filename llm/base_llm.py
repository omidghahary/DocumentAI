from abc import ABC, abstractmethod
from models.llm_response_model import LLMResponseModel

class BaseLLM(ABC):

    @abstractmethod
    def generate(self, messages: list[dict]) -> LLMResponseModel:
        """
        Generate response from LLM.
        messages format:
        [
            {
                "role": "system",
                "content": "..."
            },
            {
                "role": "user",
                "content": "..."
            }
        ]
        """
        return LLMResponseModel(
            text="Mock response",
            prompt_tokens=12,
            completion_tokens=7,
            model="mock"
            )