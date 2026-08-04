from prompting.simple_prompt_builder import SimplePromptBuilder
from models.context_model import ContextModel
from models.prompt_model import PromptModel

def test_simple_prompt_builder_builds_prompt():

    builder = SimplePromptBuilder()
    context = ContextModel(
        text="network failure detected",
        source_chunks=[1,2],
        token_count=5
    )
    prompt = builder.build(context)
    assert isinstance(prompt, PromptModel)
    assert "network failure detected" in prompt.text