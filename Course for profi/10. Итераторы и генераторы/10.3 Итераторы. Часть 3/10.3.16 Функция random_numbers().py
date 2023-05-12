from random import randint


random_numbers = lambda left, right: iter(lambda: randint(left, right), right + 1)
