def fizzbuzz(x):
    if (x % 3 == 0 and x % 5 == 0):
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)


fizzbuzz(15)
fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(7)
