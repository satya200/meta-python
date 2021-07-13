#!/usr/bin/env python3

def main():
    test_block()
    check_condition()

w = 15

def test_block():
    x = 42
    y = 73
    if x > y:
        print('x > y: x is {} and y is {}'.format(x, y))
    else:
        print(f'x < y: x is {x} and y is {y}')

def check_condition():
    x = 43
    y = 34
    if x > y:
        print('x > y: x is {} and y is {}'.format(x, y))
    elif x == y:
        print('x == y: x is {} and y is {}'.format(x, y))
    else:
        print('x < y: x is {} and y is {}'.format(x, y))

# Below line inform to intrpeter to check all code before executing any script
if __name__ == '__main__':main()
