#!/usr/bin/env python3

def main():
    x = kitten(5)
    kitten1(buffy = 'meow', zilla = 'grr', angel = 'rawr')
    kitten2('meow', 'grr', 'rawr')
    print(x)

def kitten(n):
    print('Mewoo')
    return n

def kitten1(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten1 says {} says {}'.format(k, kwargs[k]))
    else:
        print('Meow')

def kitten2(*args):
    if len(args):
        for k in args:
            print(k)
    else:
        print('Meow Kitten2')

if __name__ == '__main__':main()
