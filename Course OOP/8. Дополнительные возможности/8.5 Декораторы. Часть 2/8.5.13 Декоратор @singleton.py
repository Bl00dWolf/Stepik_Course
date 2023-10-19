def singleton(cls):
    cls._instance_ = None

    def new_new(self, *args, **kwargs):
        if cls._instance_ is None:
            cls._instance_ = object.__new__(self)
        return cls._instance_

    cls.__new__ = new_new
    return cls


# еще вариант
# import functools
#
#
# def singleton(cls):
#     cls_new = cls.__new__
#     cls._instance = None
#
#     @functools.wraps(cls_new)
#     def new_for_singleton(*args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#         return cls._instance
#
#     cls.__new__ = new_for_singleton
#     return cls