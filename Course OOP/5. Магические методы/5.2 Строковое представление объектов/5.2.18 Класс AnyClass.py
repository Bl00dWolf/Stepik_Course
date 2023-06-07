class AnyClass:
    def __init__(self, **kwargs):
        [self.__setattr__(key, value) for key, value in kwargs.items()]

    def __repr__(self):
        if self.__dict__:
            res = 'AnyClass('
            for k, v in self.__dict__.items():
                res = res + f"{k}={repr(v)}, "
            return res[:-2] + ')'
        else:
            return 'AnyClass()'

    def __str__(self):
        if self.__dict__:
            res = 'AnyClass: '
            for k, v in self.__dict__.items():
                res = res + f"{k}={repr(v)}, "
            return res[:-2]
        else:
            return 'AnyClass: '


# еще вариант:
# class AnyClass:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#     def __str__(self):
#         return f'AnyClass: {", ".join(self._attrs())}'
#
#     def __repr__(self):
#         return f'AnyClass({", ".join(self._attrs())})'
#
#     def _attrs(self):
#         return [f'{k}={repr(v)}' for (k, v) in self.__dict__.items()]