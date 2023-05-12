def to_binary(number: int) -> bin:
    if number // 2 == 0:
        return str(number % 2)
    else:
        return str(to_binary(number // 2)) + str(number % 2)
