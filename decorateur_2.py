from functools import wraps
import time


def outer(n):
    def inner(func):
        @wraps(func)
        def wrapper(x):
            """ DOC of wrapper """
            return func(x ** n)
        return wrapper
    return inner


@outer(5)
def f(x):
    """ DOC of f """
    return x


start_time = time.time()
for i in range(11):
    print(f"f({i}) = {f(i)}")

end_time = time.time()
time_lapse = end_time - start_time
print(f"Time Lapse : {time_lapse}")
