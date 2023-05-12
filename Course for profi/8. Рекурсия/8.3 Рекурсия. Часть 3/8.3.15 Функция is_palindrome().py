def is_palindrome(string: str) -> bool:
    if len(string) in (0, 1):
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return is_palindrome(string[1:-1])


# print(is_palindrome('stepik'))
