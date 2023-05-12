# def choose_plural(amount, declensions):
#     if str(amount).endswith('0'):
#         return f'{amount} {declensions[2]}'
#     elif str(amount).endswith('1'):
#         return f'{amount} {declensions[0]}'
#     elif str(amount).endswith('2') or str(amount).endswith('3') or str(amount).endswith('4'):
#         return f'{amount} {declensions[1]}'
#
# print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))

def choose_plural(amount, variants):
    variant = 2
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    return '{} {}'.format(amount, variants[variant])