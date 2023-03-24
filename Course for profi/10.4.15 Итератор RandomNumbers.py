from random import randint


class RandomNumbers:
    def __init__(self, left: int, right: int, n):
        self.left, self.right, self.n = left, right, n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n:
            self.n -= 1
            return randint(self.left, self.right)
        else:
            raise StopIteration


iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))