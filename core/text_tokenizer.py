import re

class TextTokenizer:

    def tokenize(self, text: str) -> list[str]:
        return re.findall(r"\b[\w]+(?:\.[\w]+)*\b", text.lower())