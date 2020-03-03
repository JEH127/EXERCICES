def fac(n):
    if n < 0:
        return "ERREUR"

    elif n == 0:
        return 1

    else:
        # récursivité
        return n * fac(n-1)


for n in range(11):
    print(f"{n}! = {fac(n)}")
