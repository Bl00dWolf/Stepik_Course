from collections.abc import MutableSequence


class SortedList(MutableSequence):
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self._seq_ = sorted(list(iterable))

    def __str__(self):
        return f'{self.__class__.__name__}({self._seq_})'

    def __getitem__(self, item):
        if isinstance(item, int | slice):
            return self._seq_[item]
        return NotImplemented

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        del self._seq_[key]

    def discard(self, item):
        count = self._seq_.count(item)
        if count > 0:
            for i in range(count):
                self._seq_.remove(item)

    def __len__(self):
        return len(self._seq_)

    def append(self, value):
        raise NotImplementedError

    extend = append

    def insert(self, key, value):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __iter__(self):
        return iter(self._seq_)

    def __contains__(self, item):
        return item in self._seq_

    def add(self, item):
        self._seq_.append(item)
        self._seq_.sort()

    def update(self, obj):
        self._seq_.extend(obj)
        self._seq_.sort()

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(sorted(self._seq_ + other._seq_))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(sorted(self._seq_ * other))
        return NotImplemented

    def __reversed__(self):
        raise NotImplementedError

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self._seq_ += other._seq_
            self._seq_.sort()
            return self
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self._seq_ *= other
            self._seq_.sort()
            return self
        return NotImplemented
