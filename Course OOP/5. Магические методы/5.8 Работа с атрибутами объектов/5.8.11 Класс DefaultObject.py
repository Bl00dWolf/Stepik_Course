class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        [self.__setattr__(n, v) for n, v in kwargs.items()]

    def __getattr__(self, item):
        return self.default

# еще вариант
#
# class DefaultObject:
#     def __init__(self, default=None, **kwargs):
#         self.default = default
#         self.__dict__.update(kwargs)
#
#     def __getattr__(self, name):
#         return self.default
