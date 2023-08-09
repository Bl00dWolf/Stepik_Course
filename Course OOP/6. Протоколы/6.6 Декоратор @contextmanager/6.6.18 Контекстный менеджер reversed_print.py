from contextlib import contextmanager
import sys


@contextmanager
def reversed_print():
    st_out = sys.stdout.write
    sys.stdout.write = lambda x: st_out(x[::-1])
    yield
    sys.stdout.write = st_out