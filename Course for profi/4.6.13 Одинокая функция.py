import pickle
import sys

with open(input(), 'rb') as file:
    funcc = pickle.load(file)

print(funcc(*list(map(str.strip, sys.stdin))))