def palindromes():
    num = 0
    while True:
        num += 1
        if str(num) == str(num)[::-1]:
            yield num


# generator = palindromes()
# numbers = [next(generator) for _ in range(30)]
#
# print(*numbers)