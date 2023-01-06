d1, d2, d3 = int(input()), int(input()), int(input())

circle_path_distance = d1 + d3 + d2
middle_distance = sorted([d1, d2, d3])[1]
balanced_distance = min(d1, d2, d3) * 2 + middle_distance * 2

print(min(circle_path_distance, balanced_distance))

# Еще вариант
# d1, d2, d3 = [int(input()) for _ in range(3)]
#
# print(min(d1 + d2 + d3, 2*(d1 + d2), 2*(d2 + d3), 2*(d1 + d3)))