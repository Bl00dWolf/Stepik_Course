class Grouper:
    def __init__(self, iterable, key):
        self._key = key
        self._dic = {}

        for v in iterable:
            self._dic.setdefault(self._key(v), []).append(v)

    def add(self, item):
        self._dic.setdefault(self._key(item), []).append(item)

    def group_for(self, item):
        return self._key(item)

    def __len__(self):
        return len(self._dic)

    def __iter__(self):
        yield from self._dic.items()

    def __contains__(self, item):
        return item in self._dic

    def __getitem__(self, item):
        return self._dic[item]
