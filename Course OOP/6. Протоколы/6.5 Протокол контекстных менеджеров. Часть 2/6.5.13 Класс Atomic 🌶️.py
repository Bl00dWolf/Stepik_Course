from copy import deepcopy, copy


class Atomic:
    def __init__(self, data: list | set | dict, deep: bool = False):
        self._deep = deep
        self._safe_data = data
        if deep:
            self._data = deepcopy(self._safe_data)
        else:
            self._data = copy(self._safe_data)

    def __enter__(self):
        return self._data

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if exc_type is not None:
        # self._safe_data = self._data
        pass


numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[1]

print(numbers)
