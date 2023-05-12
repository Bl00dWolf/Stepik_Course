from collections import Counter

av_books = Counter(input().split())

for _ in range(int(input())):
    clas, price = input().split()
    if av_books.get(clas):
        av_books[clas] -= 1
        av_books['money'] += int(price)
print(av_books['money'])
