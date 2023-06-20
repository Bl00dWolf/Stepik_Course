class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.attrs_num = len(self.__dict__)

    def __delattr__(self, item):
        object.__delattr__(self, item)
        object.__setattr__(self, 'attrs_num', object.__getattribute__(self, 'attrs_num') - 1)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)
        object.__setattr__(self, 'attrs_num', object.__getattribute__(self, 'attrs_num') + 1)

# еще вариант
# class AttrsNumberObject:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#     def __getattr__(self, name):
#         if name == 'attrs_num':
#             return len(self.__dict__) + 1