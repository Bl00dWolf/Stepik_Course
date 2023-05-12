def primes(left: int, right: int):
    if left == 1:
        left += 1
    while left <= right:
        flag = True
        for num in range(2, left):
            if left % num == 0:
                flag = False
                break
        if flag:
            yield left
        left += 1


generator = primes(1, 15)
print(*generator)
