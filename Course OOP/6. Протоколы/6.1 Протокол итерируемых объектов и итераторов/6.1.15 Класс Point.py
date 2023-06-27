class Point:
    def __init__(self, x: int | float, y: int | float, z: int | float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.z})'

    def __iter__(self):
        yield from (self.x, self.y, self.z)
