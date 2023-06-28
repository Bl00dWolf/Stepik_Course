class SparseArray:
    def __init__(self, default):
        self.default = default
        self._lst = []

    def __getitem__(self, key):
        if key < len(self._lst):
            return self._lst[key]
        else:
            return self.default

    def __setitem__(self, key, value):
        if key >= len(self._lst):
            off = key + 1 - len(self._lst)
            self._lst.extend([self.default] * off)
        self._lst[key] = value
