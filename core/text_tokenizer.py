import string

class TextTokenizer:

    def tokenize(self, text: str) -> list[str]:
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator).lower().split()