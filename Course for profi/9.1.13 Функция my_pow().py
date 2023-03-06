def my_pow(number: int) -> int:
    return sum(int(num) ** i for i, num in enumerate(str(number), 1))


print(my_pow(123))
