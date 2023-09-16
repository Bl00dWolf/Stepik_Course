class LowerString(str):
    def __new__(cls, obj=''):
        instance = super().__new__(cls, obj.__str__().lower())
        return instance
