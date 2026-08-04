from abc import ABC, abstractmethod
from models.prompt_model import PromptModel

class BasePromptFormatter(ABC):

    @abstractmethod
    def format(self, prompt: PromptModel) -> list[dict]:
        """
        Convert PromptModel into provider-specific chat messages.
        """
        raise NotImplementedError