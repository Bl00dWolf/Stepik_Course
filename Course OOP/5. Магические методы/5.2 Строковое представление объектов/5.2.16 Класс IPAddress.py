from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        raise TypeError('Неверные данные')

    @__init__.register(str)
    def from_str(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register(list)
    @__init__.register(tuple)
    def from_tuple_list(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"

    def __str__(self):
        return self.ipaddress
