def print_operation_table(operation, rows: int, cols: int) -> None:
    matrix = [[0] * (cols) for _ in range(rows)]
    for i in range(rows):
        print()
        for j in range(cols):
            matrix[i][j] = operation(i + 1, j + 1)
            print(matrix[i][j], end=' ')


# еще вариант
# def print_operation_table(operation, rows, cols):
#     for i in range(1, rows + 1):
#         print(*map(operation, [i] * cols, range(1, cols + 1)))