class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return self.length * 2 + self.width * 2

    def get_area(self):
        return self.length * self.width

    perimeter = property(get_perimeter)
    area = property(get_area)
