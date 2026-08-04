from models.prompt_model import PromptModel
from prompting.base_prompt_formatter import BasePromptFormatter

class SimplePromptFormatter(BasePromptFormatter):

    def format(self, prompt: PromptModel) -> list[dict]:
        return [
            {
                "role": "system",
                "content": "You are a document analysis assistant."
            },
            {
                "role": "user",
                "content": prompt.text
            }
        ]