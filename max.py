def max(x):
    maxi = x[0]

    for i in range(len(x)):
        if x[i] > maxi:
            maxi = x[i]
    return maxi


nums = [1, 7, 3]
print(max(nums))
