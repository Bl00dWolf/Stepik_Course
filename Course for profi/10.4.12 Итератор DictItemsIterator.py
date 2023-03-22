class DictItemsIterator:
    def __init__(self, data: dict):
        self.data = data
        self.index = -1
        self.keys = tuple(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.data) - 1:
            raise StopIteration
        return self.keys[self.index], self.data.get(self.keys[self.index])

#
# еще вариант
# class DictItemsIterator:
#     def __init__(self, data):
#         self.data = data
#         self.keys = iter(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         key = next(self.keys)
#         return key, self.data[key]

# pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
#
# print(*pairs)
