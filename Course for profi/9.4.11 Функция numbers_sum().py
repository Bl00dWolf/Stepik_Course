def numbers_sum(elems: list) -> int | float:
    """
    Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.:
    """
    return sum(elem for elem in elems if isinstance(elem, (int, float)))

