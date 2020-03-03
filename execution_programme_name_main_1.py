def outer(n):
    def inner(func):
        def wrapper(x):
            print(f"{func.__name__}")
            return func(x ** n)
        return wrapper
    return inner


@outer(5)
def f(x):
    print(x)


if __name__ == "__main__":
    f(3)
    print("Exécution directe du programme")
else:
    print("Exécution du programme avec importation")
