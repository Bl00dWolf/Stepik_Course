total = 0

with open('data.txt', encoding='utf-8') as file: # 2
    for _ in file.readlines(): #3
        total = total + 1 #1

print(total)