class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        if not self.b ** 2 - 4 * self.a * self.c < 0:
            return (-self.b - (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)
        return None

    @property
    def x2(self):
        if not self.b ** 2 - 4 * self.a * self.c < 0:
            return (-self.b + (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)
        return None

    @property
    def view(self):
        if self.a < 0:
            a_view = f'-{abs(self.a)}x^2 '
        else:
            a_view = f'{self.a}x^2 '

        if self.b < 0:
            b_view = f'- {abs(self.b)}x'
        else:
            b_view = f'+ {self.b}x'

        if self.c < 0:
            c_view = f' - {abs(self.c)}'
        else:
            c_view = f' + {self.c}'
        return a_view + b_view + c_view

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, coef: tuple[int, int, int]):
        self.a, self.b, self.c = coef[0], coef[1], coef[2]
