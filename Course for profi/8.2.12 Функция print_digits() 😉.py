def print_digits(number: int) -> None:
    def print_num(num):
        if num:
            print_num(num.pop())
            print(num)

    print_num(list(str(number)))


print_digits(12345)
