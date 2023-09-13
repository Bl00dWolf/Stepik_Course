class Counter:
    def __init__(self, start: int = 0):
        self.start = start
        self._counter = start

    @property
    def value(self):
        return self._counter

    @value.setter
    def value(self, value):
        self._counter = value

    def inc(self, num: int = 1):
        self.value += num

    def dec(self, num: int = 1):
        self.value -= num
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    def dec(self, num: int = 1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start: int = 0, limit: int = 10):
        Counter.__init__(self, start)
        self.limit = limit

    def inc(self, num: int = 1):
        self.value += num
        if self.value > self.limit:
            self.value = self.limit

# еще вариант:
# class Counter:
#     def __init__(self, start=0):
#         self.value = start
#
#     def inc(self, n=1):
#         self.value += n
#
#     def dec(self, n=1):
#         self.value = max(self.value - n, 0)
#
#
# class NonDecCounter(Counter):
#     def dec(self, n=1):
#         return None
#
#
# class LimitedCounter(Counter):
#     def __init__(self, start=0, limit=10):
#         Counter.__init__(self, start)
#         self.limit = limit
#
#     def inc(self, n=1):
#         self.value = min(self.value + n, self.limit)
