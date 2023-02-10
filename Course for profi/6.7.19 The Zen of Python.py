from collections import Counter

with open('pythonzen.txt') as file:
    data = file.read().strip()

counts = Counter()
for cha in data:
    if cha.lower() in 'qwertyuiopasdfghjklzxcvbnm':
        counts[cha.lower()] += 1

[print(f'{k}: {v}') for k, v in sorted(counts.items())]

# еще вариант
# from collections import Counter
#
# with open('pythonzen.txt', 'r', encoding='utf-8') as file:
#     letters = Counter([letter.lower() for letter in file.read() if letter.isalpha()])
#
# for letter in sorted(letters):
#     print(f'{letter}: {letters[letter]}')
