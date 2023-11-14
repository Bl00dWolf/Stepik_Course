# from copy import deepcopy, copy
#
#
# class Atomic:
#     def __init__(self, data: list | set | dict, deep: bool = False):
#         self._deep = deep
#         self._safe_data = data
#         if deep:
#             self._data = deepcopy(self._safe_data)
#         else:
#             self._data = copy(self._safe_data)
#
#     def __enter__(self):
#         return self._data
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # if exc_type is not None:
#         # self._safe_data = self._data
#         pass

import copy


class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.deep = deep
        self.backup = None

    def __enter__(self):
        self.backup = copy.deepcopy(self.data) if self.deep else self.data.copy()
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.data = self.backup
        return True


# TEST_5:
numbers = {1, 2, 3, 4, 5}

with Atomic(numbers) as atomic:
    atomic.add(6)
    atomic.append(7)  # добавление элемента с помощью несуществующего метода

print(sorted(numbers))

with Atomic(numbers) as atomic:
    atomic.add(6)

print(sorted(numbers))
