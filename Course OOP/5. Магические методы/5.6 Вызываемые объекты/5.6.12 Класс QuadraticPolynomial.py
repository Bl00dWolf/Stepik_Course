class QuadraticPolynomial:
    def __init__(self, a: int | float, b: int | float, c: int | float):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x: int | float):
        return self.a * x ** 2 + self.b * x + self.c
