import itertools as it

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

vars_buy = 0
for size in range(1, len(wallet) + 1):
    combs = it.combinations(wallet, r=size)
    for combination in set(combs):
        if sum(combination) == 100:
            vars_buy += 1
print(vars_buy)