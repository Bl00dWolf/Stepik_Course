import functools


def auto_repr(args, kwargs):
    def wrapper(cls):
        old_repr = cls.__repr__

        @functools.wraps(old_repr)
        def new_repr(self):
            args_values = [getattr(self, x) for x in args]
            kwargs_dict = {k: v for k, v in zip(kwargs, [getattr(self, x) for x in kwargs])}
            kwargs_str = [f'{k}={repr(v)}' for (k, v) in kwargs_dict.items()]
            if kwargs_str:
                return f'{cls.__name__}({", ".join(map(str, args_values))}, {", ".join(kwargs_str)})'
            else:
                return f'{cls.__name__}({", ".join(args_values)})'

        cls.__repr__ = new_repr
        return cls

    return wrapper


@auto_repr(args=['name', 'surname'], kwargs=[])
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


person = Person('Gvido', 'van Rossum')

print(person)
