class PermaDict:
    def __init__(self, data: dict = None):
        if data is None:
            data = {}
        self._dict = dict(data)

    def keys(self):
        return self._dict.keys()

    def values(self):
        return self._dict.values()

    def items(self):
        return self._dict.items()

    def __len__(self):
        return len(self._dict)

    def __getitem__(self, item):
        return self._dict[item]

    def __iter__(self):
        yield from self._dict

    def __setitem__(self, key, value):
        if key not in self._dict:
            self._dict[key] = value
        else:
            raise KeyError('Изменение значения по ключу невозможно')

    def __delitem__(self, key):
        del self._dict[key]
