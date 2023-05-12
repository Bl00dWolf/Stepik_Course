import sys

data = [l.strip('\n') for l in sys.stdin.readlines()]
code_lines = [data[i] for i in range(len(data)) if data[i].strip().find('#') != 0]
[print(line) for line in code_lines]

# еще решение
# [sys.stdout.write(i) for i in sys.stdin if not i.lstrip().startswith('#')]

