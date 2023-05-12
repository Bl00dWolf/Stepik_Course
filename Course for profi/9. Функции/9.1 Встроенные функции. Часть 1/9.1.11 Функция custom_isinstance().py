def custom_isinstance(objects: list, typeinfo: type | set) -> int:
    return sum(map(lambda x: 1 if isinstance(x, typeinfo) else 0, objects))

# еще вариант
# def custom_isinstance(objects, typeinfo):
#     return sum(isinstance(i, typeinfo) for i in objects)