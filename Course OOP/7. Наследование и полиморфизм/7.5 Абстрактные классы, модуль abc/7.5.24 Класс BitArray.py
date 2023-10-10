from collections.abc import Sequence
from copy import deepcopy


class BitArray(Sequence):
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self.__elems__ = deepcopy(iterable)

    def __repr__(self):
        return f'{[elem for elem in self.__elems__]}'

    def __len__(self):
        return len(self.__elems__)

    def __getitem__(self, item):
        return self.__elems__[item]

    def __invert__(self):
        temp_lst = []
        for i in range(len(self.__elems__)):
            if self.__elems__[i] == 0:
                temp_lst.append(1)
            elif self.__elems__[i] == 1:
                temp_lst.append(0)
        return self.__class__(temp_lst)

    def __or__(self, other):
        if isinstance(other, self.__class__) and len(self.__elems__) == len(other):
            temp = []
            for i in range(len(self.__elems__)):
                if self.__elems__[i] == 1 or other[i] == 1:
                    temp.append(1)
                else:
                    temp.append(0)
            return self.__class__(temp)
        return NotImplemented

    def __and__(self, other):
        if isinstance(other, self.__class__) and len(self.__elems__) == len(other):
            temp = []
            for i in range(len(self.__elems__)):
                if self.__elems__[i] == 1 and other[i] == 1:
                    temp.append(1)
                else:
                    temp.append(0)
            return self.__class__(temp)
        return NotImplemented

# еще вариант, явно лучше и верней
# from collections.abc import Sequence
#
#
# class BitArray(Sequence):
#     def __init__(self, iterable=()):
#         self._data = list(iterable)
#
#     def __str__(self):
#         return str(self._data)
#
#     def __len__(self):
#         return len(self._data)
#
#     def __getitem__(self, index):
#         if isinstance(index, (int, slice)):
#             return self._data[index]
#         return NotImplemented
#
#     def __invert__(self):
#         return type(self)(int(not item) for item in self._data)
#
#     def __or__(self, other):
#         if isinstance(other, type(self)):
#             return type(self)(self_item | other_item for self_item, other_item in zip(self._data, other._data))
#         return NotImplemented
#
#     def __and__(self, other):
#         if isinstance(other, type(self)):
#             return type(self)(self_item & other_item for self_item, other_item in zip(self._data, other._data))
#         return NotImplemented