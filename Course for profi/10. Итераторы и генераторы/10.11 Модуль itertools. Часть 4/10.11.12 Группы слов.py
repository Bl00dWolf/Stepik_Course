from itertools import groupby

data = input().split()
gp = groupby(sorted(data, key=len), key=len)

print(*[f'{k} -> {", ".join(sorted(v))}' for k, v in gp], sep='\n')