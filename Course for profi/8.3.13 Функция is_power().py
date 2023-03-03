def is_power(number: int) -> bool:
    if not float(number).is_integer():
        return False
    if number == 0:
        return False
    elif number == 1:
        return True
    else:
        return is_power(number / 2)


# print(is_power(15))
# print(is_power(512))
# print(is_power(1))

# еще варианты
# is_power = lambda n: n == 1 if n <= 1 else is_power(n / 2)
#
# def is_power(number):
#     if number == 1:
#         return True
#     elif number < 1:
#         return False
#     else:
#         return is_power(number / 2)