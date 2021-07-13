#!/usr/bin/env python3

from decimal import *

x = 7
a = 8
b = 9
s = 'Satya'.capitalize()
q = 'Satya'.upper()
t = 'Satya'.lower()
y = f'seven {a:<09} {b:>09}'
print(f'x is {x}')
print(type(x))
print(type(s))
print(f's = {s} and q = {q} and t = {t}')
print(f'y = {y}')

# python is 2 type int and float type
k = Decimal('.10')
l = Decimal('.30')
z = k + k + k - l
print(f'z is {z}')
print(type(z))

c = (1, 'two', 3.0, [4, 'four'], 5)
d = (1, 'two', 3.0, [4, 'four'], 5)
print('c is {}'.format(c))
print(type(c[1]))
print(type(d[1]))
# Below both id are same
print(id(c))
print(id(d))

if c[0] is d[0]:
    print('Yes')
else:
    print('No')

if isinstance(c, tuple):
    print('Yes')
elif isinstance(c, list):
    print('list')
else:
    print('Nope')
