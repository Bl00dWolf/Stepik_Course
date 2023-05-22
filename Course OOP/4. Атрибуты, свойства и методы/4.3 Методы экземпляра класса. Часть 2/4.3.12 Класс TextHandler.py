class TextHandler:
    def __init__(self):
        self.words = []

    def add_words(self, text: str):
        self.words.extend([word for word in text.split()])

    def get_shortest_words(self):
        if self.words:
            min_len = len(min(self.words, key=len))
            return [word for word in self.words if len(word) == min_len]
        return []

    def get_longest_words(self):
        if self.words:
            max_len = len(max(self.words, key=len))
            return [word for word in self.words if len(word) == max_len]
        return []
