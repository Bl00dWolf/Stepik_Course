def hash_function(obj):
    # первое преобразование
    obj = str(obj)
    temp1 = 0
    k = -1

    # если длинна нечетная, то средний элемент плюсуем
    if len(obj) % 2 != 0:
        temp1 += ord(obj[(len(obj) // 2)])

    # умножаем и плюсуем до середины
    for i in range(len(obj) // 2):
        temp1 += ord(obj[i]) * ord(obj[k])
        k -= 1

    # второе преобразование
    temp2 = 0
    for i in range(len(obj)):
        if i % 2 == 0:
            temp2 += ord(obj[i]) * (i + 1)
        else:
            temp2 -= ord(obj[i]) * (i + 1)

    return (temp1 * temp2) % 123456791

# еще вариант
# def hash_function(obj):
#     obj = str(obj)
#     temp1 = temp2 = 0
#     for i in range(len(obj) // 2):
#         temp1 += ord(obj[i]) * ord(obj[-(i + 1)])
#     if len(obj) % 2:
#         temp1 += ord(obj[len(obj) // 2])
#     for i, c in enumerate(obj, 1):
#         temp2 += ord(c) * i * ((-1) ** (i + 1))
#     return temp1 * temp2 % 123456791

