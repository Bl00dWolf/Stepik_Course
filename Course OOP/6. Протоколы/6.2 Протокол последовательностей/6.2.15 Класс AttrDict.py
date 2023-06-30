from copy import deepcopy


class AttrDict:
    def __init__(self, data: dict = None):
        if data is None:
            data = {}
        self._data = deepcopy(data)
        self.__dict__.update(deepcopy(data))
        # self._data = data

    def __iter__(self):
        yield from self._data.keys()

    def __getitem__(self, item):
        return self._data[item]

    def __len__(self):
        return len(self._data)

    def __setitem__(self, key, value):
        self.__dict__[key] = value
        self._data[key] = value

# еще вариант
# from copy import deepcopy
#
#
# class AttrDict:
#     def __init__(self, data=None):
#         if data is None:
#             data = {}
#         self.data = deepcopy(data)
#
#     def __len__(self):
#         return len(self.data)
#
#     def __setitem__(self, key, value):
#         self.data[key] = value
#
#     def __getitem__(self, item):
#         return self.data[item]
#
#     def __getattr__(self, item):
#         return self.data[item]
# 
#     def __iter__(self):
#         return iter(deepcopy(self.data))