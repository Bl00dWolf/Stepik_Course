from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month

    def __repr__(self):
        return f'{self.__class__.__name__}({self.year}, {self.month})'

    def __str__(self):
        return f'{self.year}-{self.month}'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.year == other.year and self.month == other.month
        elif isinstance(other, tuple):
            return (self.year, self.month) == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.year < other.year or (self.year == other.year and self.month < other.month)
        elif isinstance(other, tuple):
            return (self.year, self.month) < other
        return NotImplemented
