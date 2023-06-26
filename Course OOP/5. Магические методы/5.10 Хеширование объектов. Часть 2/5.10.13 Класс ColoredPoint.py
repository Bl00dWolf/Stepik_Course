class ColoredPoint:
    def __init__(self, x: int | float, y: int | float, color: str):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        raise AttributeError

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        raise AttributeError

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        raise AttributeError

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {repr(self.color)})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.color == other.color
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y, self.color))

# еще вариант:
#
#
# class ColoredPoint:
#     def __init__(self, x, y, color):
#         self._x = x
#         self._y = y
#         self._color = color
#
#     @property
#     def x(self):
#         return self._x
#
#     @property
#     def y(self):
#         return self._y
#
#     @property
#     def color(self):
#         return self._color
#
#     @property
#     def _fields(self):
#         return self._x, self._y, self._color
#
#     def __repr__(self):
#         return "ColoredPoint({}, {}, '{}')".format(*self._fields)
#
#     def __eq__(self, other):
#         if isinstance(other, ColoredPoint):
#             return self._fields == other._fields
#         return NotImplemented
#
#     def __hash__(self):
#         return hash(self._fields)