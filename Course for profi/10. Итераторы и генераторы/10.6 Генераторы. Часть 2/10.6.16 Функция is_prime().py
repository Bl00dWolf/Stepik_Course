def is_prime(number: int):
    if number == 1:
        return False
    return all(False for num in range(2, number) if number % num == 0)


print(is_prime(7))
