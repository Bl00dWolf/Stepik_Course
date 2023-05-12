def bee(n):
    if n > 0:
        print(n)
        bee(n - 5)
    print(n)

bee(int(input()))