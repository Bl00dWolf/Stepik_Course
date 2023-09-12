class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._name = name
        self._default = default

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]
        else:
            if self._default is None:
                raise AttributeError('Атрибут не найден')
            else:
                return self._default

    def __set__(self, instance, value):
        if isinstance(value, int) and value >= 0:
            instance.__dict__[self._name] = value
        else:
            raise ValueError('Некорректное значение')
