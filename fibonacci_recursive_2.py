def fib(n):
    if n <= 0:
        return "ERREUR"

    elif n == 1:
        return 1

    elif n == 2:
        return 1

    else:
        return fib(n - 2) + fib(n - 1)


var = int(input("Entrez un nombre entier > 0 : "))

print(f"fib(0) à fib({var}) : \n")

for n in range(var + 1):
    print(f"fiboonacci({n}) = {fib(n)}")
