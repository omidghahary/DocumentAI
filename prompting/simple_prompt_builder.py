from models.context_model import ContextModel
from models.prompt_model import PromptModel
from prompting.base_prompt_builder import BasePromptBuilder

class SimplePromptBuilder(BasePromptBuilder):

    def build(self, context: ContextModel) -> PromptModel:
        prompt_text = (
            "You are a document analysis assistant.\n\n"
            "Analyze the following document context:\n\n"
            f"{context.text}"
        )
        return PromptModel(text=prompt_text)