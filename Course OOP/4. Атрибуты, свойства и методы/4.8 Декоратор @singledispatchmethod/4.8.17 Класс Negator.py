from functools import singledispatchmethod

class Negator:
    @singledispatchmethod
    @staticmethod
    def neg():
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _neg(value):
        return -value

    @neg.register(bool)
    @staticmethod
    def _neg(value):
        return True if not value else False