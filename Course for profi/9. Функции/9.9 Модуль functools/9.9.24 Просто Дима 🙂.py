from functools import cache
import sys


@cache
def leks_word(word: str):
    return ''.join(sorted(word))


for word in sys.stdin.readlines():
    print(leks_word(word.strip()))
