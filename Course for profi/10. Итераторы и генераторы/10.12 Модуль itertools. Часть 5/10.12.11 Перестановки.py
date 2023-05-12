import itertools as it

s = input()
res = sorted(list(set(it.permutations(s, r=len(s)))))
print(*[''.join(i) for i in res], sep='\n')
