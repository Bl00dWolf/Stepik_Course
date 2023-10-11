def get_method_owner(cls, method: str):
    for cl in cls.mro():
        if method in cl.__dict__:
            return cl
    return None
