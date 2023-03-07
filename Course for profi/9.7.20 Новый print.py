old_print = print

def upper(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()