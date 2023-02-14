def get_max_index(numbers):
    max_index = len(numbers) - 1 #4
    max_value = numbers[-1]

    for index, value in enumerate(numbers, 0): #1
        if value > max_value: #2
            max_index = index
            max_value = value

    return max_index #3