class Progression:
    ar_type = None

    def __init__(self, first: int | float, diff: int | float):
        self.first = first
        self.__curnum__ = self.first
        self.diff = diff

    def __iter__(self):
        return self

    def __next__(self):
        if self.__class__.ar_type == 'Arithmetic':
            res = self.__curnum__
            self.__curnum__ += self.diff
        elif self.__class__.ar_type == 'Geometric':
            res = self.__curnum__
            self.__curnum__ *= self.diff
        return res


class ArithmeticProgression(Progression):
    ar_type = 'Arithmetic'


class GeometricProgression(Progression):
    ar_type = 'Geometric'