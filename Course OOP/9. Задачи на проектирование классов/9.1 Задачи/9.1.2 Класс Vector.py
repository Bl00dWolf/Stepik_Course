class Vector:
    def __init__(self, *args: int | float):
        self.coords = list(args)

    def __repr__(self):
        return f'({", ".join(map(str, self.coords))})'

    def __same_sized__(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError('Векторы должны иметь равную длину')

    def __add__(self, other):
        if isinstance(other, self.__class__):
            self.__same_sized__(other)
            points = []
            for x, y in zip(self.coords, other.coords):
                points.append(x + y)
            return self.__class__(*points)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            self.__same_sized__(other)
            points = []
            for x, y in zip(self.coords, other.coords):
                points.append(x - y)
            return self.__class__(*points)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            self.__same_sized__(other)
            points = []
            for x, y in zip(self.coords, other.coords):
                points.append(x * y)
            return sum(points)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            self.__same_sized__(other)
            return self.coords == other.coords
        return NotImplemented

    def norm(self) -> int | float:
        return sum(map(lambda x: x ** 2, self.coords)) ** 0.5
