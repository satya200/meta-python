#!/usr/bin/env python3

# Below is seq
x = [ 1, 2, 3, 4, 5 ]
x[2] = 43
for i in x:
    print('Seq i is {}'.format(i))

# Below is touple
y = (1, 2, 3, 4, 5)
#y[2] = 43 # This is error because We can not  modify touple data member
for i in y:
    print('touple i is {}'.format(i))
#
# Below table.
z = {'one':1, 'Two': 2}
for v,w in z.items():
    print('v: {} and w:{}'.format(v, w))
