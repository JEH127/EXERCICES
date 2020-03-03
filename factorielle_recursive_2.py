def fac(n):  # récursivité de la fonction
    if n < 0:
        return "ERREUR"

    elif n == 0:
        return 1

    else:
        return n * fac(n-1)


var = int(input("Entrez un nombre entier >= 0 : "))

print(f"Calcul 0! à {var}! : \n")

for n in range(var + 1):
    print(f"{n}! = {fac(n)}")
