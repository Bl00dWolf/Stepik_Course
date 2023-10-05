import abc
import math


class Validator:
    @abc.abstractmethod
    def validate(self, obj):
        pass

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name not in instance.__dict__:
            raise AttributeError('Атрибут не найден')
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        self.__class__.validate(self, value)
        instance.__dict__[self._name] = value


class Number(Validator):
    def __init__(self, minvalue: int | float = -math.inf, maxvalue: int | float = math.inf):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, obj):
        if not isinstance(obj, int | float):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if obj < self.minvalue:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        if obj > self.maxvalue:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')


class String(Validator):
    def validate(self, obj):
        if not isinstance(obj, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if len(obj) < self.minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        if len(obj) > self.maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        if not self.predicate(obj):
            raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')

    def __init__(self, minsize: int = -1, maxsize: int = math.inf, predicate=lambda x: True):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

# еще вариант
# from abc import ABC, abstractmethod
#
#
# class Validator(ABC):
#     def __set_name__(self, owner, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self._attr not in obj.__dict__:
#             raise AttributeError('Атрибут не найден')
#         return obj.__dict__[self._attr]
#
#     def __set__(self, obj, value):
#         self.validate(value)
#         obj.__dict__[self._attr] = value
#
#     @abstractmethod
#     def validate(self, value):
#         pass
#
#
# class Number(Validator):
#     def __init__(self, minvalue=None, maxvalue=None):
#         self.minvalue = minvalue
#         self.maxvalue = maxvalue
#
#     def validate(self, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError('Устанавливаемое значение должно быть числом')
#         if self.minvalue is not None and value < self.minvalue:
#             raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
#         if self.maxvalue is not None and value > self.maxvalue:
#             raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
#
#
# class String(Validator):
#     def __init__(self, minsize=None, maxsize=None, predicate=None):
#         self.minsize = minsize
#         self.maxsize = maxsize
#         self.predicate = predicate
#
#     def validate(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Устанавливаемое значение должно быть строкой')
#         if self.minsize is not None and len(value) < self.minsize:
#             raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
#         if self.maxsize is not None and len(value) > self.maxsize:
#             raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
#         if self.predicate is not None and not self.predicate(value):
#             raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')
