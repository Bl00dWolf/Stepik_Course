class Wordplay:
    def __init__(self, words: list = None):
        if words is None:
            self.words = []
        else:
            self.words = words

    def add_word(self, word: str):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n: int):
        return [word for word in self.words if len(word) == n]
