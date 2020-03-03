def add(x, y=10):
    return x + y


print(add)  # <function add at 0x03CB9420>

print(add.__name__)  # add

print(add.__module__)  # __main__

print(add.__defaults__)  # (10,)

print(add.__code__)
# <code object add at 0x00B3DD30, file "c:\Users\jamalh\Desktop\CODE_JOB\EXERCICES\j_pydata_2_fonction.py", line 1>

print(add.__code__.co_code)  # bytecode => b'|\x00|\x01\x17\x00S\x00'

print(add.__code__.co_nlocals)  # nombre variables locales => 2

print(add.__code__.co_name)  # add

print(add.__code__.co_names)  # ()

print(dir(add.__code__))
"""
[
'__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
'__init__', '__init_subclass__', '__le__', '__lt__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars',
'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags',
'co_freevars', 'co_kwonlyargcount', 'co_lnotab', 'co_name', 'co_names',
'co_nlocals', 'co_stacksize','co_varnames'
]

"""

print(add.__code__.co_varnames)  # ('x', 'y')
