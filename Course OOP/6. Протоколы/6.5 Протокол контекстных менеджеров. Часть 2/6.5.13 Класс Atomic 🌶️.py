from copy import deepcopy


class Atomic:
    def __init__(self, data: list | set | dict, deep: bool = False):
        self.data = data
        self.deep = deep
        self.__save__ = deepcopy(self.data) if self.deep else self.data.copy()

    def __enter__(self):
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            if isinstance(self.data, list):
                self.data[:] = self.__save__
            if isinstance(self.data, dict):
                for k, v in self.__save__.items():
                    self.data[k] = v
            if isinstance(self.data, set):
                self.data.clear()
                self.data.update(self.__save__)
        return True


# еще вариант
# import copy
#
#
# class Atomic:
#     def __init__(self, data, deep=False):
#         self.original = data
#         self.copy = copy.deepcopy if deep else copy.copy
#
#         if isinstance(data, list):
#             self.original_update = self.original.extend
#         elif isinstance(data, (set, dict)):
#             self.original_update = self.original.update
#
#     def __enter__(self):
#         self.data = self.copy(self.original)
#         return self.data
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.original.clear()
#             self.original_update(self.data)
#         return True

# еще вариант
# from copy import copy, deepcopy
#
#
# class Atomic:
#     def __init__(self, data, deep=False):
#         self.data = data
#         self.deep = deep
#         self.copy = deepcopy(self.data) if deep else copy(self.data)
#
#     def __enter__(self):
#         return self.copy
#
#     def __exit__(self, exc_type, exc_val, traceback):
#         if exc_type is None:
#             self.data.clear()
#             if isinstance(self.data, list):
#                 self.data.extend(self.copy)
#             else:
#                 self.data.update(self.copy)
#         return True
