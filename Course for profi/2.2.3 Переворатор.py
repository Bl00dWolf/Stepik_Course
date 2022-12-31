n, X, Y, A, B = [int(d) - 1 for d in input().split()]
nums = [i for i in range(1, n + 2)]

nums[X:Y + 1] = nums[X:Y + 1][::-1]
nums[A:B + 1] = nums[A:B + 1][::-1]

print(*nums)
