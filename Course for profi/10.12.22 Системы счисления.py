import itertools as it

n, m = int(input()), int(input())
chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

curset = chars[:n]
combs = it.product(curset, repeat=m)
for comb in combs:
    print(''.join(comb), end=' ')