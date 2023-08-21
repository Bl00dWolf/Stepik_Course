from contextlib import contextmanager


@contextmanager
def safe_open(filename: str, mode: str = 'r'):
    error = None
    file = None
    try:
        file = open(filename, mode)
    except Exception as err:
        error = err
    yield file, error
    if file:
        file.close()