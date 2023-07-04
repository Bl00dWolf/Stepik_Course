class MutableString:
    def __init__(self, string: str = ''):
        self._strlst = [s for s in string]

    def lower(self):
        self._strlst = list(map(str.lower, self._strlst))

    def upper(self):
        self._strlst = list(map(str.upper, self._strlst))

    def __str__(self):
        return ''.join(self._strlst)

    def __repr__(self):
        return f'{self.__class__.__name__}({repr("".join(self._strlst))})'

    def __len__(self):
        return len(self._strlst)

    def __iter__(self):
        yield from self._strlst

    def __setitem__(self, key, value):
        self._strlst[key] = value
        self._strlst = [s for s in ''.join(self._strlst)]

    def __delitem__(self, key):
        del self._strlst[key]

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._strlst[item]
        elif isinstance(item, slice):
            return self.__class__(''.join(self._strlst[item]))

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(''.join(self._strlst) + ''.join(other._strlst))
        return NotImplemented
