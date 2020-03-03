def addition(*numbers):
    somme = 0
    for n in numbers:
        somme += n
    return somme


print(addition(1, 2, 3, 4, 5))
