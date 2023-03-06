obj = eval(input())

if isinstance(obj, list):
    print(obj[-1])
elif isinstance(obj, tuple):
    print(obj[0])
elif isinstance(obj, set):
    print(len(obj))

# еще вариант
# n = eval(input())
# print(eval({list: 'n[-1]', tuple: 'n[0]', set: 'len(n)'}[type(n)]))