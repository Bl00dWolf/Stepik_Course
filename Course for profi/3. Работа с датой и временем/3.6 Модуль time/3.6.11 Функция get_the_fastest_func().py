import time


def get_the_fastest_func(funcs, arg):
    min_time = 99999999.9
    fast_f = None
    for func in funcs:
        start = time.perf_counter()
        func(arg)
        total = time.perf_counter() - start
        if min_time > total:
            min_time = total
            fast_f = func
    return fast_f


# def slow(arg):
#     time.sleep(3)
#
#
# def sred(arg):
#     time.sleep(2)
#
#
# def fast(arg):
#     time.sleep(1)
#
#
# funcs = [slow, fast, sred]
#
# print(get_the_fastest_func(funcs, 0))
