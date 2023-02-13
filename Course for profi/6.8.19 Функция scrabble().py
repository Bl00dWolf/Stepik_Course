from collections import Counter


def scrabble(symbols: str, word: str) -> bool:
    w_syms = Counter(word.lower())
    s_syms = Counter(symbols.lower())
    if s_syms >= w_syms:
        return True
    return False

# более изящная запись
#
# def scrabble(symbols, word):
#     return Counter(word.lower()) <= Counter(symbols.lower())
