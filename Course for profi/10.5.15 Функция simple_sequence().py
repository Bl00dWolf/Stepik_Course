def simple_sequence():
    num = 0
    while True:
        num += 1
        for nnum in range(num):
            yield num