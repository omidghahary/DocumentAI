import pytest
from prompting.base_prompt_builder import BasePromptBuilder

def test_base_prompt_builder_is_abstract():
    with pytest.raises(TypeError):
        BasePromptBuilder()

def test_base_prompt_builder_build_method_is_required():
    class DummyPromptBuilder(BasePromptBuilder):
        pass
    with pytest.raises(TypeError):
        BasePromptBuilder()