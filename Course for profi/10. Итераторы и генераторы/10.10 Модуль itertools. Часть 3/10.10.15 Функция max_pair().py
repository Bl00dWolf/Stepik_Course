import itertools as it

# def max_pair(iterable):
#     return sum(max(it.pairwise(iterable), key=lambda x: x[0] + x[1]))


max_pair = lambda iterable: sum(max(it.pairwise(iterable), key=sum))

print(max_pair([1, 8, 2, 4, 3]))
