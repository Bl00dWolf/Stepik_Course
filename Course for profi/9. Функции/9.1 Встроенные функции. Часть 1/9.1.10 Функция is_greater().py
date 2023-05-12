def is_greater(lists: list, number: int) -> bool:
    return any(sum(listl) > number for listl in lists)
