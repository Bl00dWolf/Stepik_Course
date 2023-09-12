class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self._times = times

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name not in instance.__dict__:
            raise AttributeError('Атрибут не найден')
        elif self._times <= 0:
            raise MaxCallsException('Превышено количество доступных обращений')
        self._times -= 1
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value
