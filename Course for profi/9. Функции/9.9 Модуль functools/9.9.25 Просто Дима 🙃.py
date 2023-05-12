from functools import cache


@cache
def ways(n: int) -> int:
    if n <= 3:
        return 1
    elif n == 4:
        return 2
    else:
        return ways(n-1) + ways(n-3) + ways(n-4)