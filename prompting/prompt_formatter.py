from models.prompt_model import PromptModel

class SimplePromptFormatter:

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