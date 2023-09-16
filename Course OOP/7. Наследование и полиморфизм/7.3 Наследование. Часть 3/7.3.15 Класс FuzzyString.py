class FuzzyString(str):
    def __eq__(self, other):
        if isinstance(other, FuzzyString | str):
            if self.lower() == other.lower():
                return True
            return False
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, FuzzyString | str):
            if self.lower() != other.lower():
                return True
            return False
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, FuzzyString | str):
            if self.lower() < other.lower():
                return True
            return False
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, FuzzyString | str):
            if self.lower() > other.lower():
                return True
            return False
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, FuzzyString | str):
            if self.lower() <= other.lower():
                return True
            return False
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, FuzzyString | str):
            if self.lower() >= other.lower():
                return True
            return False
        return NotImplemented

    def __contains__(self, item):
        if isinstance(item, FuzzyString | str):
            if item.lower() in self.lower():
                return True
            return False
        return NotImplemented


# гениальное решение:
#
#
# class FuzzyString(str):
#     def __new__(cls, obj):
#         instance = super().__new__(cls, obj)
#         for oper in map(lambda s: f'__{s}__', ('eq', 'ne', 'lt', 'le', 'gt', 'ge', 'contains')):
#             setattr(cls, oper, cls._comparator(oper))
#         return instance
#
#     @staticmethod
#     def _comparator(oper):
#         def _compare(self, other):
#             if not isinstance(other, (str, self.__class__)):
#                 return NotImplemented
#             return getattr(self.lower(), oper)(other.lower())
#
#         return _compare