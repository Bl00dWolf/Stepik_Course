from collections import Counter

counts = sorted(Counter(input().split(',')).items())
mlen = len(max(counts, key=lambda x: len(x[0]))[0])

for word, num in counts:
    price = 0
    for char in word:
        if char != ' ':
            price += ord(char)
    print(f'{word.ljust(mlen)}: {price} UC x {num} = {price * num} UC')
