from re import fullmatch, sub


class CaseHelper:
    @staticmethod
    def is_snake(string):
        pattern = r'[a-z]+(_[a-z]+)*'
        return bool(fullmatch(pattern, string))

    @staticmethod
    def is_upper_camel(string):
        pattern = r'([A-Z][a-z]+)+'
        return bool(fullmatch(pattern, string))

    @staticmethod
    def to_snake(string):
        pattern = r'[a-z]?[A-Z]'
        repl = lambda m: '_'.join(m.group().lower())
        return sub(pattern, repl, string)

    @staticmethod
    def to_upper_camel(string):
        pattern = r'_([a-z])'
        repl = lambda m: m.group(1).upper()
        return sub(pattern, repl, string.capitalize())


def snake_case(attrs: bool = False):
    def decor(obj):
        params = []
        vals = {}

        for param in obj.__dict__:
            if not param.startswith('__') and not callable(getattr(obj, param)) == attrs:
                vals[param] = getattr(obj, param)
                params.append(param)

        for param in params:
            setattr(obj, CaseHelper.to_snake(param), vals[param])
            delattr(obj, param)
        return obj

    return decor

# еще вариант
# import re
# from typing import Callable
#
#
# def snake_case(attrs=False):
#     regex_object = re.compile(r'_?\B([A-Z])')
#
#     def wrapper(cls, *args, **kwargs):
#         class_attributes = list(cls.__dict__.keys())
#         for attribute in class_attributes:
#             if any((
#                     attribute.startswith('__') and attribute.endswith('__'),
#                     not isinstance(cls.__dict__[attribute], Callable) and not attrs
#             )):
#                 continue
#             setattr(cls, regex_object.sub(r'_\1', attribute).lower(), cls.__dict__[attribute])
#             delattr(cls, attribute)
#         return cls
#
#     return wrapper

# еще варик
# from functools import wraps
# from inflection import camelize, underscore
#
# def snake_case(attrs=False):
#     def decorator(cls):
#         for i,j in list(cls.__dict__.items()):
#             if i.count('_') < 4 and not callable(j) == attrs:
#                 attr = j
#                 delattr(cls,i)
#                 setattr(cls,underscore(i),attr)
#         return cls
#     return decorator
