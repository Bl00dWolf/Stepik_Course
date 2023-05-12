import sys

print(max(eval(line.strip()) for line in sys.stdin.readlines()))

# еще вариант
# import sys
#
# print(max(map(eval, sys.stdin)))
