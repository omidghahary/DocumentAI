from abc import ABC, abstractmethod
from models.context_model import ContextModel
from models.prompt_model import PromptModel

class BasePromptBuilder(ABC):

    @abstractmethod
    def build(self, context: ContextModel) -> PromptModel:
        raise NotImplementedError