class Numbers:
    def __init__(self):
        self.num_l = []

    def add_number(self, num: int):
        self.num_l.append(num)

    def get_even(self):
        return list(filter(lambda x: x % 2 == 0, self.num_l))

    def get_odd(self):
        return list(filter(lambda x: x % 2 != 0, self.num_l))
