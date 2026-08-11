import pytest
from core.text_tokenizer import TextTokenizer

@pytest.fixture
def tokenizer():
    return TextTokenizer()

def test_text_tokenizer_creation(tokenizer):
    assert tokenizer is not None

def test_text_tokenizer_normalizes_text(tokenizer):
    tokens = tokenizer.tokenize("Network, configuration!")
    assert tokens == ["network", "configuration"]

def test_text_tokenizer_empty_text(tokenizer):
    tokens = tokenizer.tokenize("")
    assert tokens == []