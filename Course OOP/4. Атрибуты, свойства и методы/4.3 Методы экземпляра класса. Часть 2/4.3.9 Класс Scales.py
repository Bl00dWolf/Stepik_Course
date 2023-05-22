class Scales:
    def __init__(self):
        self.lweight, self.rweight = 0, 0

    def add_right(self, weight: int | float):
        self.rweight += weight

    def add_left(self, weight: int | float):
        self.lweight += weight

    def get_result(self):
        if self.rweight == self.lweight:
            return 'Весы в равновесии'
        elif self.rweight > self.lweight:
            return 'Правая чаша тяжелее'
        elif self.rweight < self.lweight:
            return 'Левая чаша тяжелее'
