n = int(input())

triangle = []
for i in range(n):
    triangle.append([1] + [0] * n)

for i in range(1, n):
    for j in range(1, i + 1):
        triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

# кривой вывод =)
# [[print(j, end=' ') for j in i if j != 0] for i in triangle]

for i in triangle:
    print()
    for j in i:
        if j != 0:
            print(j, end=' ')
