class ReversibleString:
    def __init__(self, string: str):
        self.string = string

    def __repr__(self):
        return self.string

    def __neg__(self):
        return self.__class__(self.string[::-1])
