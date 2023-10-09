from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self.__lst__ = []
        for el in args:
            if isinstance(el, str):
                elem1, elem2 = el.split('-')
                self.__lst__.extend(range(int(elem1), int(elem2) + 1))
            else:
                self.__lst__.append(el)

    def __getitem__(self, item):
        return self.__lst__[item]

    def __len__(self):
        return len(self.__lst__)
