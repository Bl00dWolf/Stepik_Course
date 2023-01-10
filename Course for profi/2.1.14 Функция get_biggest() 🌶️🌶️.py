def get_biggest(numbers: list[int]) -> int:
    if numbers:
        max_len_num = max(numbers, key=lambda x: len(str(x)))
        num_str = sorted(map(lambda x: str(x), numbers), key=lambda x: x * max_len_num, reverse=True)
        return int(''.join(num_str))
    else:
        return -1


print(get_biggest([7, 71, 72]))
