# params >= 1 => tuple : (param1, param2, ...)
def f(*args):
    print(args)


# paramètres nommés => dictionnaire : {'params nommes' : valeur}
def g(**kwargs):
    print(kwargs)


def h(a, b):
    print(a, b)


f(1, 2, 3)  # => (1, 2, 3)

g(x=1, y=2, z=3)  # => {'x': 1, 'y': 2, 'z': 3}

L = [1, 2]
d = {'a': 3, 'b': 4}

h(*L)
h(**d)
