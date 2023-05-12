nums = [i for i in range(1, int(input()) + 1)]

n_dict = {}
for i in range(len(nums)):
    nums[i] = sum(map(int, list(str(nums[i]))))
    n_dict[nums[i]] = n_dict.setdefault(nums[i], 0) + 1

print(max(n_dict.values()))
