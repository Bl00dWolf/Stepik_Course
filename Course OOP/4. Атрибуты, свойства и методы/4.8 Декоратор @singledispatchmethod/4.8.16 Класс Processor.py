from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register
    @staticmethod
    def _process(data: int):
        return data * 2

    @process.register
    @staticmethod
    def _process(data: float):
        return data * 2

    @process.register
    @staticmethod
    def _process(data: str):
        return data.upper()

    @process.register
    @staticmethod
    def _process(data: list):
        return sorted(data)

    @process.register
    @staticmethod
    def _process(data: tuple):
        return tuple(sorted(data))
