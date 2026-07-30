from dataclasses import dataclass

@dataclass(frozen=True)
class LLMResponseModel:
    text: str
    prompt_tokens: int = 0
    completion_tokens: int = 0
    model: str = ""