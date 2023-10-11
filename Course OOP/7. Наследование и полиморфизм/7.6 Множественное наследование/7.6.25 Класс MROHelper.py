class MROHelper:
    @staticmethod
    def len(cls):
        return len(cls.mro())

    @staticmethod
    def class_by_index(cls, n: int = 0):
        return cls.mro()[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.mro().index(parent)
