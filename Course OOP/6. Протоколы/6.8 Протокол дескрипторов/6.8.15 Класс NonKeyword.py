from keyword import kwlist


class NonKeyword:
    def __init__(self, name):
        self._attr = name

    def __get__(self, instance, owner):
        if self._attr in instance.__dict__:
            return instance.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        if value not in kwlist:
            instance.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')

    def __delete__(self, instance):
        del self.__dict__[instance]


# еще вариант:
# from keyword import kwlist
#
#
# class NonKeyword:
#     def __init__(self, name):
#         self._attr = name
#
#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self._attr not in obj.__dict__:
#             raise AttributeError('Атрибут не найден')
#         return obj.__dict__[self._attr]
#
#     def __set__(self, obj, value):
#         if value in kwlist:
#             raise ValueError('Некорректное значение')
#         obj.__dict__[self._attr] = value