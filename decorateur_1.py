from functools import wraps


def decorate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """ DOC of wrapper """
        return func(*args, **kwargs)
    return wrapper


@decorate
def f(x):
    """ DOC of f """
    print(x)


f(3)
print(f.__doc__)
