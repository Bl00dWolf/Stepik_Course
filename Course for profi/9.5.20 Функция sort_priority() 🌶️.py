def sort_priority(values: list[int], group: list[int] | tuple[int] | set[int]) -> None:
    tmp_l = []
    values.sort()
    for num in sorted(group):
        if num in values:
            tmp_l.append(num)

    for i, num in enumerate(tmp_l):
        values.pop(values.index(num))
        values.insert(i, num)


# еще вариант, намного лучше =)
#
# def sort_priority(numbers, group):
#     numbers.sort(key=lambda x: (x not in group, x))
