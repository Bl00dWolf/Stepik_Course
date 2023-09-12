from random import randint


class RandomNumber:
    def __init__(self, start: int, end: int, cache=False):
        self._start = start
        self._end = end
        self._cache = cache
        self._num = randint(self._start, self._end)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        raise AttributeError('Изменение невозможно')

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._cache:
            return self._num
        return randint(self._start, self._end)
