class NonNegativeObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if isinstance(v, (int, float)) and v < 0:
                v = abs(v)
            self.__dict__[k] = v

# еще вариант
#
# class NonNegativeObject:
#     def __init__(self, **kwargs):
#         for name, value in kwargs.items():
#             setattr(self, name, value)
#
#     def __setattr__(self, name, value):
#         if isinstance(value, (int, float)):
#             value = abs(value)
#         object.__setattr__(self, name, value)
