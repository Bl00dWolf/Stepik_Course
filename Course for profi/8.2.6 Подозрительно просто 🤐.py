def num_1_to_100():
    def res(n):
        if n <= 100:
            print(n)
            res(n + 1)

    res(1)


num_1_to_100()
