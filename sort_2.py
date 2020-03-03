def sort(x):
    for i in range(len(x) - 1, 0, -1):
        for j in range(i):
            if x[j] > x[j + 1]:  # swap
                temp = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp
    return x


nums = [5, 3, 8, 6, 7, 2]
print(sort(nums))
