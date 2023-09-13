class Validator:
    def __init__(self, obj):
        self.obj = obj

    @staticmethod
    def is_valid():
        return None


class NumberValidator(Validator):
    def is_valid(self):
        return isinstance(self.obj, int | float)
