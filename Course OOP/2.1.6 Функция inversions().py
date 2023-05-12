def inversions(sequence: list | range) -> int:
    total = 0
    obj = list(enumerate(sequence))
    for idx, num in obj:
        for idx2, num2 in obj:
            if idx2 > idx and num2 < num:
                total += 1
    return total

sequence = [3, 1, 4, 2]

print(inversions(sequence))
