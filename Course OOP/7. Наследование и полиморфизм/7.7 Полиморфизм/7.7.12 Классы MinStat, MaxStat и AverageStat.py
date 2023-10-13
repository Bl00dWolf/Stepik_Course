import abc


class Stat:

    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self._it_ = list(iterable)

    def add(self, value: int | float) -> None:
        self._it_.append(value)

    @abc.abstractmethod
    def result(self, func=bool) -> int | float | None:
        if self._it_:
            return func(self._it_)
        return None

    def clear(self) -> None:
        self._it_ = []


class MaxStat(Stat):
    def result(self, func=bool) -> int | float | None:
        return super().result(max)


class MinStat(Stat):
    def result(self, func=bool) -> int | float | None:
        return super().result(min)


class AverageStat(Stat):
    def result(self, func=bool) -> int | float | None:
        if self._it_:
            return super().result(sum) / len(self._it_)
        return None

# еще вариант:
#
#
# class Stat(list):
#     add = getattr(list, 'append')
#
#
# class MinStat(Stat):
#     def result(self):
#         return min(self, default=None)
#
#
# class MaxStat(Stat):
#     def result(self):
#         return max(self, default=None)
#
#
# class AverageStat(Stat):
#     def result(self):
#         if self:
#             return sum(self) / len(self)
