from string import ascii_lowercase, ascii_uppercase


def verification(login: str, password: str, success, failure):
    if set(password).isdisjoint(ascii_lowercase) and set(password).isdisjoint(ascii_uppercase):
        failure(login, 'в пароле нет ни одной буквы')
    elif set(password).isdisjoint(ascii_uppercase):
        failure(login, 'в пароле нет ни одной заглавной буквы')
    elif set(password).isdisjoint(ascii_lowercase):
        failure(login, 'в пароле нет ни одной строчной буквы')
    elif set(password).isdisjoint('1234567890'):
        failure(login, 'в пароле нет ни одной цифры')
    else:
        success(login)


# еще вариант
# def verification(login, password, success, failure):
#     vd = {str.isalpha: 'в пароле нет ни одной буквы',
#           str.islower: 'в пароле нет ни одной строчной буквы',
#           str.isupper: 'в пароле нет ни одной заглавной буквы',
#           str.isdigit: 'в пароле нет ни одной цифры'}
#     for f in vd:
#         if not any(f(i) for i in password):
#             return failure(login, vd[f])
#     success(login)