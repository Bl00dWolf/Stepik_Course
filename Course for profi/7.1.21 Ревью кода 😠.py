def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        if char in vowels:  # 1
            char = char.upper()  # 2
        swapped_string += char

    return swapped_string  # 3
