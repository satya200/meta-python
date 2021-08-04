#!/usr/bin/env python3

print('Hellow, world'.capitalize())
print('Hellow'.upper())
print('Hellow'.swapcase())
print('Hellow {}'.format(42 * 7))

s1 = "Hellow"
s2 = s1.upper()
s3 = "Hi"

# If we use upper methode it will create different object
print(id(s1))
print(id(s2))

print(s1+s3)

s = 'This is a long string with a bounch of words.'
l = s.split()
s2 = ':'.join(l)
print(s2)
