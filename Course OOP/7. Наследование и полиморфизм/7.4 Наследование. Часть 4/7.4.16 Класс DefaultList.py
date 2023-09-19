from collections import UserList


class DefaultList(UserList):
    def __init__(self, iterable=None, default=None):
        if iterable is None:
            iterable = []
        super().__init__(iterable)
        self._default = default

    def __getitem__(self, item):
        try:
            return self.data[item]
        except IndexError:
            return self._default
