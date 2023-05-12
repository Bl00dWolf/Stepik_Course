def make_html(tag: str):
    def decor(func):
        from functools import wraps

        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>' + func(*args, **kwargs) + f'</{tag}>'

        return wrapper

    return decor
