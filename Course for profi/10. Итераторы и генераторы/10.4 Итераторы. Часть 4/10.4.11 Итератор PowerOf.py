class PowerOf:
    def __init__(self, number: int):
        self.number = number
        self.pow = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.pow += 1
        return self.number ** self.pow


# power_of_two = PowerOf(2)
#
# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))
