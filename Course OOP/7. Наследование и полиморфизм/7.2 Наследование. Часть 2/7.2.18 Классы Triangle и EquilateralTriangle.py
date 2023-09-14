class Triangle:
    def __init__(self, a: int | float, b: int | float, c: int | float):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, side: int | float):
        super().__init__(side, side, side)
