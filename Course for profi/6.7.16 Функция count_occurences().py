from collections import Counter

def count_occurences(word: str, words: str) -> int:
    count = Counter([word.lower() for word in words.split()])
    return count[word.lower()]