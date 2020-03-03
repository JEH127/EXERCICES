def sort(x):
    for i in range(len(x) - 1, 0, -1):
        for j in range(i):
            if x[j] > x[j + 1]:  # swap
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


nums = [1, 7, 3]
print(sort(nums))
