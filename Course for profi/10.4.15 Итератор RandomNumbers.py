class RandomNumbers:
    def __init__(self, left: int, right: int, n):
        self.left, self.right, self.n = left, right, n

    def __iter__(self):
        return self

    def __next__(self):
        pass