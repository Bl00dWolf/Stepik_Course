def print_digits(number: int) -> None:
    def print_num(num):
        if num:
            print(num.pop(0))
            print_num(num)

    print_num(list(str(number)))