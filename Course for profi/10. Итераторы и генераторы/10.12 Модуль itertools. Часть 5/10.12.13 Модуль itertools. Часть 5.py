import itertools as it

wallet = [100, 50, 20, 10, 5]

price_tovar = 100
min_nominal = min(wallet)
max_len = price_tovar // min_nominal

vars_buy = 0
for size in range(1, max_len + 1):
    combs = it.combinations_with_replacement(wallet, r=size)
    for combination in set(combs):
        if sum(combination) == 100:
            vars_buy += 1
print(vars_buy)