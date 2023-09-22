from collections import UserString


class MutableString(UserString):
    def __init__(self, seq):
        super().__init__(seq)
        self._str = seq

    def __str__(self):
        return f'{self._str}'

    def __setitem__(self, key, value):
        self._str = self._str[:key] + value + self._str[key + 1:]

    def __delitem__(self, key):
        self._str = self._str[:key] + self._str[key + 1:]

    def lower(self):
        self._str = super().lower()

    def upper(self):
        self._str = super().upper()

    def sort(self, key=None, reverse=False):
        self._str = ''.join(sorted(str(self._str), key=key, reverse=reverse))

# нормальное решение:
# from collections import UserString
#
#
# class MutableString(UserString):
#     def __setitem__(self, index, value):
#         data_as_list = list(self.data)
#         data_as_list[index] = value
#         self.data = "".join(data_as_list)
#
#     def __delitem__(self, index):
#         data_as_list = list(self.data)
#         del data_as_list[index]
#         self.data = "".join(data_as_list)
#
#     def upper(self):
#         self.data = self.data.upper()
#
#     def lower(self):
#         self.data = self.data.lower()
#
#     def sort(self, key=None, reverse=False):
#         self.data = "".join(sorted(self.data, key=key, reverse=reverse))