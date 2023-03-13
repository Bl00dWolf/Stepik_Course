def transpose(matrix):
    nm = []
    for row in zip(*matrix):
        nm.append(list(row))
    return nm

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# for row in transpose(matrix):
#     print(row)

# еще вариант
# transpose = lambda matrix: list(map(list, zip(*matrix)))
