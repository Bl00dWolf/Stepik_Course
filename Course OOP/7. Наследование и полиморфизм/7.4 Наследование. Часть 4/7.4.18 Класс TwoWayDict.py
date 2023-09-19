from collections import UserDict


class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        super().__setitem__(value, key)