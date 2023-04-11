from itertools import product


def password_gen():
    for i, j, k in product(range(10), range(10), range(10)):
        yield str(i) + str(j) + str(k)
