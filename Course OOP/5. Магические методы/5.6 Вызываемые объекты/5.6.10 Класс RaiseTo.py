class RaiseTo:
    def __init__(self, degree: int):
        self.degree = degree

    def __call__(self, x: int | float):
        return x ** self.degree
