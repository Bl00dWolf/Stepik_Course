# n = int(input())
# matrix = [input().split() for _ in range(n)]

n = 3
matrix = [['0', '1', '2'],
          ['1', '2', '7'],
          ['2', '3', '4']]


def print_matrix(matrix):
    print("-" * 15)
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()


def print_matrix_rev(matrix):
    print("-" * 15)
    for c in range(len(matrix[0])):
        for r in range(len(matrix)):
            print(matrix[r][c], end=' ')
        print()


print_matrix()

flag = 'YES'
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == matrix[j][i] or i == j:
            continue
        else:
            flag = 'NO'
            break

# if matrix[1][0] == matrix[0][1]
# and matrix[2][0] = matrix[0][2]
# and matrix[2][1] = matrix[1][2]
print(flag)
