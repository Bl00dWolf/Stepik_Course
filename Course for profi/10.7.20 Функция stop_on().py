def stop_on(iterable, obj):
    it = iter(iterable)
    while True:
        try:
            v = next(it)
        except:
            break
        if v != obj:
            yield v
        else:
            break

# Еще вариант
# def stop_on(iterable: iter, obj: Any) -> Any:
#     for item in iterable:
#         if item == obj:
#             break
#         yield item

# def stop_on(iterable, obj):
#     it = iter(iterable)
#     return iter(lambda: next(it), obj)

# iterator = iter('beegeek')
# print(*stop_on(iterator, 'a'))
#
# numbers = [1, 2, 3, 4, 5]
# print(*stop_on(numbers, 4))
