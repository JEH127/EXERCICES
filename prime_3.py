liste_prime = []


def prime(num):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} : Not Prime")
            break
    else:
        print(f"{num} : Prime")
        liste_prime.append(num)


def f(n):
    if n < 2:
        print(f"{n} : Not Prime")

    else:
        for i in range(2, n + 1):
            prime(i)
        print(f"Liste Prime : {liste_prime}")


f(10)
