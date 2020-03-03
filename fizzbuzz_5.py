# nombre de 1 à 100
# nombre multiple de 3 et 5 => Fizzbuzz
# nombre multiple de 3 => Fizz
# nombre multiple de 5 => Buzz

num = 1
fizzbuzz_count = 0
fizz_count = 0
buzz_count = 0

while num <= 100:
    if (num % 3 == 0) and (num % 5 == 0):
        print("Fizzbuzz !")
        fizzbuzz_count += 1

    elif num % 3 == 0:
        print("Fizz !")
        fizz_count += 1

    elif num % 5 == 0:
        print("Buzz !")
        buzz_count += 1

    else:
        print(num)

    num += 1

print(50*"=")
print("Fizzbuzz\tFizz\t\tBuzz")
print(f"{fizzbuzz_count}\t\t{fizz_count}\t\t{buzz_count}")
