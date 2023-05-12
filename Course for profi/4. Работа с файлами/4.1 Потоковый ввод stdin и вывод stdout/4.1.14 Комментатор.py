import sys

print(len([d for d in sys.stdin.readlines() if d.strip()[0] == '#']))