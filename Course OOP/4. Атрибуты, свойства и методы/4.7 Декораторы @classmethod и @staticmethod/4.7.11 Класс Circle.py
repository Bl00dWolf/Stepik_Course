class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @classmethod
    def from_diameter(cls, diametr):
        return Circle(diametr / 2)
