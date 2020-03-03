def multiply(*numbers):
    produit = 1
    for n in numbers:
        produit *= n
    return produit


print(multiply(1, 2, 3, 4, 5))  # 120
