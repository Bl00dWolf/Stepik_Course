data = [int(i) for i in input().split()]

more_one = {}
for key in data:
    more_one[key] = more_one.setdefault(key, 0) + 1

print(*sorted(filter(lambda x: more_one.get(x) > 1, more_one)))

# Еще вариант решения
# nums = [int(i) for i in input().split()]
# print(*sorted(filter(lambda i: nums.count(i) > 1, set(nums))))