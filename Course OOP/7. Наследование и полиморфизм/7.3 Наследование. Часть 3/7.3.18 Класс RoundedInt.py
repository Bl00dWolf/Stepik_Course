class RoundedInt(int):
    def __new__(cls, num: int, even: bool = True, *args, **kwargs):
        if even:
            if num % 2 != 0:
                return super().__new__(cls, num + 1, *args, **kwargs)
            return super().__new__(cls, num, *args, **kwargs)
        else:
            if num % 2 > 0:
                return super().__new__(cls, num, *args, **kwargs)
            return super().__new__(cls, num + 1, *args, **kwargs)

# еще вариант:
#
# class RoundedInt(int):
#     def __new__(cls, num, even=True):
#         return super().__new__(cls, num + (num % 2 == even))

# еще
# class RoundedInt(int):
#     def __new__(cls, value, even=True, *args, **kwargs):
#         value += (value % 2 == 1) if even else (value % 2 == 0)
#         instance = super().__new__(cls, value)
#         return instance
