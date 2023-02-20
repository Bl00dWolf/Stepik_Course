def print_sand_watches():
    def print_line(num, size):
        if size > 4:
            print((str(num) * size).center(16))
            print_line(num + 1, size - 4)
        print((str(num) * size).center(16))

    print_line(1, 16)

print_sand_watches()