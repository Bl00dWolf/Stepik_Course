class Vector:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Vector) and self.x == other.x and self.y == other.y:
            return True
        elif isinstance(other, tuple) and len(other) == 2 and self.x == other[0] and self.y == other[1]:
            return True
        return NotImplemented

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
