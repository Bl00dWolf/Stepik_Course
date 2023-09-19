from collections import UserDict


class EasyDict(UserDict):
    def __getattr__(self, item):
        return self[item]

# еще вариант:
#
# 
# class EasyDict(dict):
#     __getattr__ = dict.__getitem__
