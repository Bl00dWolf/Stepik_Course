class SkipIterator:
    def __init__(self, iterable, n: int):
        self._it = iter(iterable)
        self.n = n
        self._count = n

    def __iter__(self):
        return self

    def __next__(self):
        while self._count != self.n:
            next(self._it)
            self._count += 1
        self._count = 0
        return next(self._it)
