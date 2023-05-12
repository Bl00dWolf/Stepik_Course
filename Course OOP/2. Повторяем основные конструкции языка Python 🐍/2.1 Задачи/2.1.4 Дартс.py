n = int(input())

for i in range(n):
    for j in range(n):
        if i <= j and i <= n - 1 - j:
            print(i + 1, end=' ')
        elif i >= j and i >= n - 1 - j:
            print(n - i,  end=' ')
        elif j <= i <= n - 1 - j:
            print(j + 1,  end=' ')
        elif j >= i >= n - 1 - j:
            print(n - j,  end=' ')
        else:
            print(0,  end=' ')
    print()

# еще вариант:
# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         print(min(i + 1, j + 1, n - i, n - j), end=' ')
#     print()