num = 1
liste_fizzbuzz = []
liste_fizz = []
liste_buzz = []

while num <= 100:
    if(num % 3 == 0 and num % 5 == 0):
        liste_fizzbuzz.append(num)

    elif num % 3 == 0:
        liste_fizz.append(num)

    elif num % 5 == 0:
        liste_buzz.append(num)

    else:
        pass

    num += 1

print(f"Fizzbuzz : {liste_fizzbuzz}")
print(f"Fizz : {liste_fizz}")
print(f"Buzz : {liste_buzz}")
