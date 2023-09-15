from functools import reduce


class Summator:
    @staticmethod
    def total(n: int):
        return sum(range(1, n + 1))


class SquareSummator(Summator):
    @staticmethod
    def total(n: int):
        return reduce(lambda x, y: x + y ** 2, range(1, n + 1))


class QubeSummator(Summator):
    @staticmethod
    def total(n: int):
        return reduce(lambda x, y: x + y ** 3, range(1, n + 1))


class CustomSummator(Summator):
    def __init__(self, m: int):
        self.m = m

    def total(self, n: int):
        return reduce(lambda x, y: x + y ** self.m, range(1, n + 1))

# нормальное решение:
#
# class Summator:
#     def transform(self, n):
#         return n
#
#     def total(self, n):
#         return sum(self.transform(i) for i in range(1, n + 1))
#
#
# class SquareSummator(Summator):
#     def transform(self, n):
#         return n ** 2
#
#
# class QubeSummator(Summator):
#     def transform(self, n):
#         return n ** 3
#
#
# class CustomSummator(Summator):
#     def __init__(self, power):
#         self.power = power
#
#     def transform(self, n):
#         return n ** self.power
