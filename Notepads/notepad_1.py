temp = input().split()
n, m = int(temp[0]), int(temp[1])
matrix = [[0] * m for _ in range(n)]

num = 0
for q in range(n * m):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i + j == q:
                num += 1
                matrix[i][j] = num

for row in matrix:
    print(*row)
