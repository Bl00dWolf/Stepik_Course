from itertools import count


def tabulate(func):
    for i in count(1):
        yield func(i)


func = lambda x: x + 10
values = tabulate(func)

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
