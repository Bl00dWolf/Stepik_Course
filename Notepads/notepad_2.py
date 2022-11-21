from random import choice

file = open('lines.txt', encoding='UTF-8')
print(choice(file.readlines()))
file.close()