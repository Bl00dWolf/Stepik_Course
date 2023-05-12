import time


def calculate_it(func, *args):
    start = time.perf_counter()
    f = func(*args)
    end = time.perf_counter()
    return f, end - start


# def add(a, b, c):
#     time.sleep(3)
#     return a + b + c
#
#
# print(calculate_it(add, 1, 2, 3))
