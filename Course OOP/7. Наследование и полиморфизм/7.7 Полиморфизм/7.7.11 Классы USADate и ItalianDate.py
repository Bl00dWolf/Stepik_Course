class USADate:
    def __init__(self, year: str, month: str, day: str):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f'{self.month:02}-{self.day:02}-{self.year}'

    def iso_format(self):
        return f'{self.year}-{self.month:02}-{self.day:02}'


class ItalianDate:
    def __init__(self, year: str, month: str, day: str):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f'{self.day:02}/{self.month:02}/{self.year}'

    def iso_format(self):
        return f'{self.year}-{self.month:02}-{self.day:02}'
