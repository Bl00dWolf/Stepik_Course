class Currency:
    __RATE = {
        'EUR': {'EUR': 1, 'USD': 1.1, 'RUB': 90},
        'USD': {'EUR': 1 / 1.1, 'USD': 1, 'RUB': 1 / 1.1 * 90},
        'RUB': {'EUR': 1 / 90, 'USD': 1 / 90 * 1.1, 'RUB': 1}
    }

    def __init__(self, value: int | float, currency: str):
        self.value = value
        self.currency = currency

    def __repr__(self):
        return f'{round(self.value, 2)} {self.currency}'

    def change_to(self, new_currency: str):
        self.value = self.value * self.__RATE[self.currency][new_currency]
        self.currency = new_currency

    def __add__(self, other):
        if isinstance(other, self.__class__):
            oth_cur = other.currency
            other.change_to(self.currency)
            res = self.__class__(self.value + other.value, self.currency)
            other.change_to(oth_cur)
            return res

        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            oth_cur = other.currency
            other.change_to(self.currency)
            res = self.__class__(self.value - other.value, self.currency)
            other.change_to(oth_cur)
            return res

        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            oth_cur = other.currency
            other.change_to(self.currency)
            res = self.__class__(self.value * other.value, self.currency)
            other.change_to(oth_cur)
            return res

        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            oth_cur = other.currency
            other.change_to(self.currency)
            res = self.__class__(self.value / other.value, self.currency)
            other.change_to(oth_cur)
            return res

        return NotImplemented
