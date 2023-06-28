class Peekable:
    def __init__(self, iterable):
        self._it = tuple(iterable)
        self._indx = 0

    def peek(self, default=StopIteration):
        if 0 <= self._indx < len(self._it):
            return self._it[self._indx]
        else:
            if default == StopIteration:
                raise StopIteration
            else:
                return default

    def __iter__(self):
        return self

    def __next__(self):
        self._indx += 1
        if self._indx > len(self._it):
            raise StopIteration
        return self._it[self._indx - 1]
