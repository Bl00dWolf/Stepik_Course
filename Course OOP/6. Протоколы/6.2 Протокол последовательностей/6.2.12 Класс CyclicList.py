from copy import deepcopy
from itertools import cycle


class CyclicList:
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self._it = deepcopy(iterable)
        self._itt = cycle(self._it)

    def append(self, item):
        self._it.append(item)
        # self._itt = cycle(self._it)

    def pop(self, idx: int = -1):
        item = self._it.pop(idx)
        # self._itt = cycle(self._it)
        return item

    def __len__(self):
        return len(self._it)

    def __next__(self):
        return next(self._itt)

    def __iter__(self):
        return self

    def __getitem__(self, item):
        while item >= len(self._it):
            item -= len(self._it)
        return self._it[item]


# еще вариант:
# from itertools import cycle
#
#
# class CyclicList:
#     def __init__(self, iterable=()):
#         self._data = list(iterable) or []
#
#     def append(self, item):
#         self._data.append(item)
#
#     def pop(self, index=None):
#         if index is None:
#             return self._data.pop()
#         return self._data.pop(index)
#
#     def __len__(self):
#         return len(self._data)
#
#     def __iter__(self):
#         yield from cycle(self._data)
#
#     def __getitem__(self, index):
#         return self._data[index % len(self._data)]
