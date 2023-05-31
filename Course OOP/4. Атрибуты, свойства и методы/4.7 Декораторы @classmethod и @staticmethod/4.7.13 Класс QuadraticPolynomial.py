class QuadraticPolynomial:
    def __init__(self, a: int | float, b: int | float, c: int | float):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable):
        return QuadraticPolynomial(*iterable)

    @classmethod
    def from_str(cls, string: str):
        a, b, c = string.split()
        return QuadraticPolynomial(float(a), float(b), float(c))
