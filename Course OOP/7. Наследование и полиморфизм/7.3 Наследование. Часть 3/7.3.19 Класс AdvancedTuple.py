class AdvancedTuple(tuple):
    def __add__(self, other):
        if isinstance(other, tuple):
            return AdvancedTuple(tuple(self) + other)
        return AdvancedTuple(tuple(self) + tuple(other))

    def __radd__(self, other):
        if isinstance(other, tuple):
            return AdvancedTuple(other + tuple(self))
        return AdvancedTuple(tuple(other) + tuple(self))

# еще вариант:
#
# class AdvancedTuple(tuple):
#     def __add__(self, other):
#         if hasattr(other, '__iter__'):
#             return AdvancedTuple(tuple(self) + tuple(other))
#         return NotImplemented
#
#     def __radd__(self, other):
#         if hasattr(other, '__iter__'):
#             return AdvancedTuple(tuple(other) + tuple(self))
#         return NotImplemented
#
#     def __iadd__(self, other):
#         if hasattr(other, '__iter__'):
#             return AdvancedTuple(tuple(self) + tuple(other))
#         return NotImplemented
#
# и еще:
# from itertools import chain
#
#
# class AdvancedTuple(tuple):
#     def __add__(self, other):
#         return AdvancedTuple(chain(self, other))
#
#     def __radd__(self, other):
#         return AdvancedTuple(chain(other, self))
