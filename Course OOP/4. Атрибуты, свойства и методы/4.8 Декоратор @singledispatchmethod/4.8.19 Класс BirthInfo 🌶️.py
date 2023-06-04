from functools import singledispatchmethod
from datetime import date


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def from_date(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def from_date(self, birth_date):
        self.birth_date = date.fromisoformat(birth_date)

    @__init__.register(tuple)
    @__init__.register(list)
    def from_date(self, birth_date):
        self.birth_date = date(*birth_date)

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
