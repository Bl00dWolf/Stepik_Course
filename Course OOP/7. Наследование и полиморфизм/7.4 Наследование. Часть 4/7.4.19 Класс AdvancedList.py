class AdvancedList(list):
    def join(self, delimiter: str = ' '):
        return delimiter.join([str(word) for word in self])

    def map(self, func):
        self[:] = list(map(lambda x: func(x), self))

    def filter(self, func):
        self[:] = list(filter(func, self))
