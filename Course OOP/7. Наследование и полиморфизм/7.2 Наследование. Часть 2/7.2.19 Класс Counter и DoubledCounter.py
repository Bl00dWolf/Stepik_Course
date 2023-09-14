class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)


class DoubledCounter(Counter):
    def inc(self, num: int = 1):
        super().inc(num * 2)

    def dec(self, num: int = 1):
        super().dec(num * 2)
