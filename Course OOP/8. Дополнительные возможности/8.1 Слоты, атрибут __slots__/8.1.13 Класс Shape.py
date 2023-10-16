from functools import total_ordering


@total_ordering
class Shape:
    __slots__ = ('name', 'color', 'area')

    def __init__(self, name: str, color: str, area: int | float):
        self.name = name
        self.color = color
        self.area = area

    def __repr__(self):
        return f'{self.color} {self.name} ({self.area})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.area == other.area
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.area < other.area
        return NotImplemented
