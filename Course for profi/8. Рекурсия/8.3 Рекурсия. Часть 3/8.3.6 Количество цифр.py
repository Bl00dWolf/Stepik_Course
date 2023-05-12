# ndg = lambda x: 1 if x < 10 else ndg(x // 10) + 1
#
# print(ndg(int(input())))


def rec(num):
    if num <= 0:
        return 0
    else:
        return 1 + rec(num // 10)


print(rec(int(input())))
