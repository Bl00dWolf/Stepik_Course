class Cycle:
    def __init__(self, iterable):
        self.predmet = iterable
        self.iterable = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        obj = next(self.iterable, None)
        if obj:
            return obj
        self.iterable = iter(self.predmet)
        return next(self.iterable)


# cycle = Cycle((0, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 0, 9, 8, 87, 5666666))
#
# for _ in range(2000):
#     next(cycle)
#
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
