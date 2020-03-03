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
    # sortie de while
    num += 1
print(30*"=")
print(f"Fizzbuzz : {fizzbuzz_count}")
print(f"Fizz : {fizz_count}")
print(f"Buzz : {buzz_count}")
