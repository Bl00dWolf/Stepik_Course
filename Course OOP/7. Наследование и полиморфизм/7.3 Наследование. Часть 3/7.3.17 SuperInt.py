class SuperInt(int):
    def __init__(self, *args):
        super().__init__()
        self._lsnums = iter([char for char in str(self) if char.isdigit()])

    def repeat(self, n: int = 2):
        if self >= 0:
            return SuperInt(str(self) * n)
        else:
            return SuperInt("-" + str(abs(self)) * n)

    def to_bin(self):
        return format(self, 'b')

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        return self

    def __next__(self):
        return SuperInt(next(self._lsnums))

# еще вариант:
# class SuperInt(int):
#     def repeat(self, n=2):
#         digit = f"{'-' * (self < 0)}{f'{abs(self)}' * n}"
#         return type(self)(digit)
#
#     def to_bin(self):
#         return f'{self:b}'
#
#     def next(self):
#         return type(self)(self + 1)
#
#     def prev(self):
#         return type(self)(self - 1)
#
#     def __iter__(self):
#         yield from map(SuperInt, str(abs(self)))
