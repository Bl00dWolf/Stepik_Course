from copy import deepcopy


# не решил
class SequenceZip:
    def __init__(self, *args):
        self._objs = deepcopy(zip(*args))
        self._it = iter(self._objs)

    def __getitem__(self, item):
        if item >= len(self):
            raise StopIteration
        for i, elem in enumerate(deepcopy(self._it)):
            if i == item:
                return elem

    def __len__(self):
        ln = 0
        it = deepcopy(self._it)
        while True:
            try:
                next(it)
                ln += 1
            except StopIteration:
                return ln


# еще вариант:
# import copy
#
#
# class SequenceZip:
#     def __init__(self, *sequences):
#         self.sequences = copy.deepcopy(sequences)
#
#     def __len__(self):
#         return min((len(s) for s in self.sequences), default=0)
#
#     def __getitem__(self, index):
#         count = -1
#         for item in self:
#             count += 1
#             if count == index:
#                 return item
#
#     def __iter__(self):
#         yield from zip(*self.sequences)