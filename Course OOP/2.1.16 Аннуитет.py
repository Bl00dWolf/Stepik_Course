def annual_return(start: int, percent: int, years: int):
    while years > 0:
        start += (start / 100 * percent)
        yield start
        years -= 1

# Еще вариант
# from typing import Iterator
#
#
# def annual_return(start: int, percentage: int, years: int) -> Iterator:
#     return (start := start * ((percentage + 100) / 100) for _ in range(years))
