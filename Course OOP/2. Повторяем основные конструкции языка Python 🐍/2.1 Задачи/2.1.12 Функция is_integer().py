def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

print(is_integer('-9f'))