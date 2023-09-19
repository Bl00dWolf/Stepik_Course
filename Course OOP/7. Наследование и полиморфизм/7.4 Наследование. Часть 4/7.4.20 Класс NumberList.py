from collections import UserList


class NumberList(UserList):
    @staticmethod
    def isvalid(number) -> None:
        if '__iter__' not in number.__dir__():
            number = [number]
        for item in number:
            if not isinstance(item, int | float):
                raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def __init__(self, iterable):
        self.isvalid(iterable)
        super().__init__(iterable)

    def __add__(self, other):
        self.isvalid(other)
        return super().__add__(other)

    def __radd__(self, other):
        self.isvalid(other)
        return super().__radd__(other)

    def __iadd__(self, other):
        self.isvalid(other)
        return super().__iadd__(other)

    def append(self, item) -> None:
        self.isvalid(item)
        super().append(item)

    def extend(self, other) -> None:
        self.isvalid(other)
        super().extend(other)

    def insert(self, i: int, item) -> None:
        self.isvalid(i)
        self.isvalid([item])
        super().insert(i, item)

    def __setitem__(self, key, value):
        self.isvalid(value)
        super().__setitem__(key, value)
