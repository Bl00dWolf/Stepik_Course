# n = int(input())
# matrix = [input().split() for _ in range(n)]

n = 3
matrix = [['8', '1', '6'],
          ['3', '5', '7'],
          ['4', '9', '2']]

# переводим все в int
matrix = [[int(elem) for elem in row] for row in matrix]


def is_gold(matrix):
    sum_gold = sum(matrix[0])
    for row in matrix:
        if sum(row) != sum_gold:
            return False
    return True


matrix_rev = []
for i in range(n):
    matrix_rev.append([])
    for j in range(n):
        matrix_rev[i].append(matrix[j][i])

sum_main, sum_add = 0, 0
for i in range(n):
    for j in range(n):
        if i == j:
            sum_main += matrix[i][j]
        if j == n - i - 1:
            sum_add += matrix[i][j]

if is_gold(matrix) and is_gold(matrix_rev) and sum_add == sum_main:
    print('YES')
else:
    print('NO')
