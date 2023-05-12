class Xrange:
    def __init__(self, start: float | int, end: float | int, step: int | float = 1):
        self.end = end
        self.start = start - step

        self.step = step
        if abs(step) != step:
            self.otric = True
        else:
            self.otric = False

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start >= self.end and not self.otric:
            raise StopIteration
        elif self.start <= self.end and self.otric:
            raise StopIteration
        return self.start


# evens = Xrange(0, 10, 2)
# print(*evens)
#
# xrange = Xrange(0, 3, 0.5)
# print(*xrange, sep='; ')
#
# xrange = Xrange(10, 1, -1)
# print(*xrange)
#
# xrange = Xrange(5, 10)
# print(*xrange)