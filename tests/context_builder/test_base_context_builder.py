import pytest
from context.base_context_builder import BaseContextBuilder
from models.context_model import ContextModel

def test_base_context_builder_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseContextBuilder()

class DummyContextBuilder(BaseContextBuilder):
    def build(self, chunks):
        return ContextModel(
            text="dummy",
            source_chunks=[],
            token_count=0,
        )

def test_dummy_context_builder_is_base_context_builder():
    builder = DummyContextBuilder()
    assert isinstance(builder, BaseContextBuilder)