def fib(n):
    if n <= 0:
        return "ERREUR"

    elif n == 1:
        return 1

    elif n == 2:
        return 1

    else:
        return fib(n - 2) + fib(n - 1)


for n in range(11):
    print(f"fib({n}) = {fib(n)}")
