class ModularTuple(tuple):
    def __new__(cls, iterable=None, size: int = 100, *args, **kwargs):
        if iterable is None:
            iterable = []
        return super().__new__(cls, map(lambda x: x % size, iterable))
