def interleave(*args):
    for iterr in zip(*args):
        yield from (elem for elem in iterr)

print(*interleave('bee', '123'))