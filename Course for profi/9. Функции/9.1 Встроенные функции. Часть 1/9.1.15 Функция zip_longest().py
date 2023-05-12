def zip_longest(*args: list, fill=None) -> list:
    for llist in args:
        while len(llist) < len(max(args, key=len)):
            llist.append(fill)
    return [item for item in zip(*args)]

# еще вариант
# def zip_longest(*args, fill=None):
#     max_len = max(map(len, args))
#     lst = [i + [fill] * (max_len - len(i)) for i in args]
#     return list(zip(*lst))