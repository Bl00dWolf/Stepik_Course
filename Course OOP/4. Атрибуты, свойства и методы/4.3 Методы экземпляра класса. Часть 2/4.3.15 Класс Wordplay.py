from copy import deepcopy


class Wordplay:
    def __init__(self, words: list = None):
        if words is None:
            self.words = []
        else:
            self.words = deepcopy(words)

    def add_word(self, word: str):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n: int):
        return [word for word in self.words if len(word) == n]

    def only(self, *args):
        res = []
        for word in self.words:
            if not {ch for ch in word}.difference({*args}):
                res.append(word)
        return res

    def avoid(self, *args):
        res = []
        for word in self.words:
            if not {ch for ch in word}.intersection({*args}):
                res.append(word)
        return res

# еще вариант
# class Wordplay:
#     def __init__(self, words=()):
#         self.words = []
#         self.words.extend(words)
#
#     def add_word(self, word):
#         self.words.append(word)
#
#     def words_with_length(self, n):
#         return [w for w in self.words if len(w) == n]
#
#     def only(self, *args):
#         return [w for w in self.words if set(w) <= set(args)]
#
#     def avoid(self, *args):
#         return [w for w in self.words if len(set(w) & set(args)) == 0]
