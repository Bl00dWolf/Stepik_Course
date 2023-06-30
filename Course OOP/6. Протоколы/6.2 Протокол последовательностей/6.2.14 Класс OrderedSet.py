class OrderedSet:
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = tuple()
        self._set = {}
        [self._set.setdefault(k, None) for k in iterable]
        self._it = iter(self._set.keys())

    def add(self, item):
        self._set[item] = None
        self._it = iter(self._set.keys())

    def discard(self, item):
        if item in self._set.keys():
            del self._set[item]
            self._it = iter(self._set.keys())

    def __len__(self):
        return len(self._set)

    def __contains__(self, item):
        return item in self._set.keys()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._it)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            s_tp, o_tp = tuple(self._set.keys()), tuple(other._set.keys())
            return len(s_tp) == len(o_tp) and s_tp == o_tp
        elif isinstance(other, set):
            return set(self._set.keys()) == other
        return NotImplemented


orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print(*orderedset)
print(len(orderedset))

orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print('python' in orderedset)
print('C++' in orderedset)

orderedset = OrderedSet()

orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)
