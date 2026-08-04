from models.context_model import ContextModel
from models.prompt_model import PromptModel
from prompting.base_prompt_builder import BasePromptBuilder

class FakePromptBuilder(BasePromptBuilder):
    def build(self, context: ContextModel) -> PromptModel:
        return PromptModel(text=context.text)

def test_base_prompt_builder_contract():
    builder = FakePromptBuilder()
    context = ContextModel(
        text="test context",
        source_chunks=[1, 2],
        token_count=10
    )
    prompt = builder.build(context)
    assert isinstance(prompt, PromptModel)
    assert prompt.text == "test context"