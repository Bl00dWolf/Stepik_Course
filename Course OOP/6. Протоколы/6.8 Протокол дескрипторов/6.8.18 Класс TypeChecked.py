class TypeChecked:
    def __init__(self, *args):
        self._types = list(args)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        if type(value) not in self._types:
            raise TypeError('Некорректное значение')
        instance.__dict__[self._name] = value

    def __get__(self, instance, owner):
        if self._name not in instance.__dict__:
            raise AttributeError('Атрибут не найден')
        return instance.__dict__[self._name]