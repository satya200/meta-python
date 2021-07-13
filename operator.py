#!/usr/bin/env python3

x = 9
y = 4

# Below will give result with floating value
res = x / y
print('result is {}'.format(res))

# Below will give result in integer  value
res = x // y
print('result is {}'.format(res))

a = 0x0a
b = 0x02
res = a & b

print(f'(hex) a is {a:02x} & b is {b:02x} = res is {res:02x}')
print(f'(bin) a is {a:08b} & b is {b:08b} = res is {res:08b}')

c = True
d = False
# Below is the collection
e = ('cat', 'dog', 'tiger')
f = 'dog'
g = 'ox'

if c and d:
    print('expression is true')
elif c or d:
    print('expression is true1')
else:
    print('expression is false')

if f in e:
    print('f present in e')
else:
    print('f not present in e')
