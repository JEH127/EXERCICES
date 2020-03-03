def fizzbuzz(x):
    if (x % 3 == 0 and x % 5 == 0):
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x


print(f"{fizzbuzz(15)} | {fizzbuzz(3)} | {fizzbuzz(5)} | {fizzbuzz(7)}")
