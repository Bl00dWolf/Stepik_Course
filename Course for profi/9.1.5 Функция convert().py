def convert(number: int) -> (str, str, str):
    return str(bin(number)).replace('0b', ''), str(oct(number)).replace('0o', ''), str(hex(number)).replace('0x',
                                                                                                            '').upper()
# def convert(n):
#     return f'{n:b}', f'{n:o}', f'{n:X}'

# print(convert(-125))
