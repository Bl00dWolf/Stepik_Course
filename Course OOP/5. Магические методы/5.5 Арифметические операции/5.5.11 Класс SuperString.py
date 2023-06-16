class SuperString:
    def __init__(self, string: str):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return self.__class__(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return self.__class__(self.string[:(len(self.string) // other)])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if other == 0:
                return self.string
            return self.__class__(self.string[:-other])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other == 0:
                return self.string
            return self.__class__(self.string[other:])
        return NotImplemented

    def __rlshift__(self, other):
        return self.__lshift__(other)

    def __rrshift__(self, other):
        return self.__rshift__(other)
