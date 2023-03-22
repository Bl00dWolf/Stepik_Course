class Square:
    def __init__(self, n: int):
        self.n = n
        self.endn = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.endn == self.n:
            raise StopIteration
        self.endn += 1
        return self.endn ** 2


# squares = Square(10)
# print(list(squares))
