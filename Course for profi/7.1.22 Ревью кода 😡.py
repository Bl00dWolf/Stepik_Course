a = int(input()) #1
b = int(input()) #2
numbers = []

for i in range(a, b + 1): #3
    if i % 7 == 0: #5
        numbers.append(i) #4

print(numbers)