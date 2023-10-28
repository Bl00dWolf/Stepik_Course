class Anything:
    def __eq__(self, other):
        return True

    __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__


def anything():
    return Anything()

# еще вариант
# class Truly: __eq__=__ne__=__lt__=__gt__=__le__=__ge__=lambda *x: True
#
# anything = Truly
