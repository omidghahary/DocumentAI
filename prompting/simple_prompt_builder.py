from abc import ABC, abstractmethod
from models.chunk_model import ChunkModel
from prompting.base_prompt_builder import BasePromptBuilder

class SimplePromptBuilder(BasePromptBuilder):

    def build(self, chunk: ChunkModel) -> list[dict]:
        return [
            {
                "role":"system",
                "content":"You are a document analysis assistant."
            },
            {
                "role":"user",
                "content": f"Analyze the following document text:\n {chunk.text}" 
            }
        ] 