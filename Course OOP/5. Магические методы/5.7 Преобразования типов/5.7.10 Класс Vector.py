class Vector:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __int__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __float__(self):
        return float((self.x ** 2 + self.y ** 2) ** 0.5)

    def __complex__(self):
        return complex(self.x, self.y)
