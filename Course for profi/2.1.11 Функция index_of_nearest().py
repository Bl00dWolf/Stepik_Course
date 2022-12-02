def index_of_nearest(numbers, number):
    if numbers:
        return numbers.index(sorted(numbers, key=lambda x: abs(number - x))[0])
    return -1
