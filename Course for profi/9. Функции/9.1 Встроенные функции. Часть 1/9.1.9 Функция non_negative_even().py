def non_negative_even(numbers: list) -> bool:
    return all(map(lambda x: True if x >= 0 and x % 2 == 0 else False, numbers))

# еще вариант
# def non_negative_even(numbers):
#     return all(i >= 0 and i % 2 == 0 for i in numbers)