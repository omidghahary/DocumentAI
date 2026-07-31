import requests
from llm.base_llm import BaseLLM
from core.config import LLMConfig
from models.llm_response_model import LLMResponseModel

class OllamaLLM(BaseLLM):

    CHAT_ENDPOINT = "/api/chat"

    def __init__(self, config: LLMConfig):
        self.config = config

    def generate(self, messages: list[dict]) -> LLMResponseModel:
        payload = self._build_payload(messages)
        response = self._send_request(payload)
        return self._parse_response(response)

    def _build_payload(self, messages: list[dict]) -> dict:
        return {
            "model": self.config.model_name,
            "messages": messages,
            "stream": False
        }
    def _send_request(self, payload: dict):
        url = f"{self.config.base_url}{self.CHAT_ENDPOINT}"
        response = requests.post(
            url,
            json=payload,
            timeout=self.config.timeout
        )
        return response

    def _parse_response(self, response) -> LLMResponseModel:
        raise NotImplementedError