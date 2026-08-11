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

def test_text_tokenizer_preserves_numbers_and_versions(tokenizer):
    tokens = tokenizer.tokenize("Python 3.11.9 v0.11.0")
    assert tokens == [
        "python",
        "3.11.9",
        "v0.11.0",
    ]

def test_text_tokenizer_removes_punctuation_but_preserves_versions(tokenizer):
    tokens = tokenizer.tokenize("Network, configuration! Python 3.11.9.")
    assert tokens == [
        "network",
        "configuration",
        "python",
        "3.11.9",
    ]

def test_text_tokenizer_handles_whitespace(tokenizer):
    tokens = tokenizer.tokenize("Network    configuration\tsettings\n timeout")
    assert tokens == [
        "network",
        "configuration",
        "settings",
        "timeout",
    ]