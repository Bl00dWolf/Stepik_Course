from functools import wraps


def ignore_exception(*posargs):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except posargs as exp:
                print(f'Исключение {exp.__class__.__name__} обработано')
            except:
                raise

        return wrapper

    return decor


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x


f(0)