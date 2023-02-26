def sum_num(num: int) -> int:
    if num == 0:
        return 0
    else:
        return num % 10 + sum_num(num // 10)


sum_num2 = lambda x: 0 if x == 0 else x % 10 + sum_num2(x // 10)

print(sum_num2(15))
