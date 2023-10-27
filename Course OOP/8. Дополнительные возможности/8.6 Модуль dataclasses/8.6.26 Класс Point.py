from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = field(default=0.0)
    y: float = field(default=0.0)
    quadrant: int = field(init=False, compare=False, default=0)

    def __post_init__(self):
        if self.x < 0 < self.y:
            self.quadrant = 2
        elif self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
        elif self.x > 0 > self.y:
            self.quadrant = 4

    def symmetric_x(self):
        return self.__class__(self.x, -self.y)

    def symmetric_y(self):
        return self.__class__(-self.x, self.y)
