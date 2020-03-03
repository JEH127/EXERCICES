from time import time


def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print(f"elapsed time = {after - before}")
        return rv
    return f


def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print(f"running {f.__name__}")
                rv = f(*args, **kwargs)
            return rv
        return wrapper
    return inner


# decorator
@ntimes(2)
def add(x, y=10):
    return x + y


@ntimes(5)
def sub(x, y=10):
    return x - y


print(f"add(10) = {add(10)}")
print(f"add(20, 30) = {add(20, 30)}")
print(f"add('a', 'b') = {add('a', 'b')}")

print(f"sub(10) = {sub(10)}")
print(f"sub(20, 30) = {sub(20, 30)}")
