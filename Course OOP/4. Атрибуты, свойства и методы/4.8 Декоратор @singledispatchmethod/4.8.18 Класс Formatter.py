from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def _format(data):
        print(f'Целое число: {data}')

    @format.register(float)
    @staticmethod
    def _format(data):
        print(f'Вещественное число: {data}')

    @format.register(tuple)
    @staticmethod
    def _format(data):
        print(f'Элементы кортежа: {", ".join(map(str, data))}')

    @format.register(list)
    @staticmethod
    def _format(data):
        print(f'Элементы списка: {", ".join(map(str, data))}')

    @format.register(dict)
    @staticmethod
    def _format(data):
        print(f'Пары словаря: {", ".join(map(str, data.items()))}')
