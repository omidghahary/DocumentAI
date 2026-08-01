
import pytest
from dataclasses import FrozenInstanceError
from models.context_model import ContextModel

@pytest.fixture
def context():
    return ContextModel(
        text="test",
        source_chunks=[1, 2],
        token_count=10
    )

def test_context_model_can_be_created(context):
    assert context is not None

def test_context_model_fields(context):
    assert context.text == "test"
    assert context.source_chunks == [1, 2]
    assert context.token_count == 10


def test_context_model_is_immutable(context):
    with pytest.raises(FrozenInstanceError):
        context.text = "New Text"

def test_context_model_default_token_count():
    context = ContextModel(
        text="test",
        source_chunks=[1]
    )

    assert context.token_count == 0