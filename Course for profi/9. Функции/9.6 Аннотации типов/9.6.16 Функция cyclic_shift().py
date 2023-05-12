def cyclic_shift(numbers: list[int | float], step: int) -> None:
    step %= len(numbers)
    for _ in range(step):
        nm = numbers.pop(-1)
        numbers.insert(0, nm)


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)

print(numbers)
