class Strip:
    def __init__(self, chars: str):
        self.chars = chars

    def __call__(self, string: str):
        return string.strip(self.chars)
