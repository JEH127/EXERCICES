from inspect import getsource, getfile


def add(x, y=10):
    return x + y


print(getsource(add))
"""

def add(x, y=10):
    return x + y

"""
print(getfile(add))  # chemin du fichier
# c:\Users\jamalh\Desktop\CODE_JOB\EXERCICES\j_pydata_3_inspect.py

print(f"add(10) = {add(10)}")  # add(10) = 20

print(f"add(20, 30) = {add(20, 30)}")
# add(20, 30) = 50 => parametre par default pas pris en compte

print(f"add('a', 'b') = {add('a', 'b')}")  # add('a', 'b') = ab
