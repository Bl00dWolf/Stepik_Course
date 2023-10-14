class Queue:
    def __init__(self, pairs: list | dict = None):
        if pairs is None:
            pairs = {}
        if isinstance(pairs, list):
            pairs = {key: value for key, value in pairs}
        self.pairs = dict(pairs)

    def __str__(self):
        return f'{self.__class__.__name__}({[*self.pairs.items()]})'

    def __len__(self):
        return len(self.pairs)

    def add(self, elem: tuple) -> None:
        if elem[0] in self.pairs:
            del self.pairs[elem[0]]
        self.pairs[elem[0]] = elem[1]

    def pop(self):
        if not self.pairs:
            raise KeyError('Очередь пуста')
        lkey = tuple(self.pairs.keys())[0]
        temp = self.pairs[lkey]
        del self.pairs[lkey]
        return lkey, temp
