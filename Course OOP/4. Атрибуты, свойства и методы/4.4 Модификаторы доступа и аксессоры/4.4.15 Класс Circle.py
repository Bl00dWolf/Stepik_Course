from math import pi


class Circle:
    def __init__(self, radius: int | float):
        self._radius = radius
        self._diameter = self._radius * 2
        self._area = self._radius ** 2 * pi

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area
