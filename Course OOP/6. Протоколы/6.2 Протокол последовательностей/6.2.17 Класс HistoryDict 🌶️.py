class HistoryDict:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self._dic = {}
        for k, v in data.items():
            self._dic.setdefault(k, []).append(v)

    def keys(self):
        return self._dic.keys()

    def values(self):
        lst = []
        for value in self._dic.values():
            if isinstance(value, list):
                lst.append(value[-1])
            else:
                lst.append(value)
        return lst

    def items(self):
        lst = []
        for k, v in self._dic.items():
            if isinstance(v, list):
                lst.append((k, v[-1]))
            else:
                lst.append((k, v))
        return lst

    def history(self, key):
        if self._dic.get(key):
            return self._dic[key]
        return []

    def all_history(self):
        return self._dic

    def __len__(self):
        return len(self._dic)

    def __setitem__(self, key, value):
        self._dic.setdefault(key, []).append(value)

    def __getitem__(self, item):
        if len(self._dic[item]) == 1:
            return self._dic[item][-1]
        return self._dic[item]

    def __delitem__(self, key):
        del self._dic[key]

    def __iter__(self):
        yield from self._dic


historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(*historydict)
print(*historydict.keys())
print(*historydict.values())
print(*historydict.items())
