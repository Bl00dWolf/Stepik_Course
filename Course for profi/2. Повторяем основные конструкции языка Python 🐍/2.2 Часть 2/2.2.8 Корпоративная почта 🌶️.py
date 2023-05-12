digits, names = '0123456789', []

for _ in range(int(input())):
    name, _ = input().split('@')
    names.append(name)

for _ in range(int(input())):
    name = input()
    counter = 1
    while name in names:
        name = name.rstrip(digits) + str(counter)
        counter += 1
    names.append(name)
    print(f'{name}@beegeek.bzz')