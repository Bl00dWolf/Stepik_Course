class Fibonacci:
    def __init__(self):
        self.nums = []
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            self.nums.append(1)
            self.index += 1
            return 1
        elif self.index == 1:
            self.nums.append(1)
            self.index += 1
            return 1
        n3 = self.nums[self.index - 1] + self.nums[self.index - 2]
        self.nums.append(n3)
        self.index += 1
        return n3


# еще вариант:
# class Fibonacci:
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a

# fibonacci = Fibonacci()
#
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
