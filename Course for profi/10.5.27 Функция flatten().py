def flatten(nested_list: list[int | list]):
    for it in nested_list:
        if isinstance(it, list):
            yield from flatten(it)
        elif isinstance(it, int):
            yield it


generator = flatten([[1, 2], [[3]], [[4], 5]])
print(*generator)
