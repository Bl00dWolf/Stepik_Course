a = int(input())
m = 0.05
p = 1000
d = 0
b = 0
while a >= b:
    d = p * m
    p += d
    b += 1
print(round(p, 2))
