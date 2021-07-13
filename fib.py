#!/usr/bin/env python3

def main():
    fib()

def fib():
    a, b = 0, 1
    #print('In side fib() a = {} and b = {}',a, b)
    while b < 10:
        #print('{}'.format(b))
        print(b, end = ' ', flush = True)
        a, b = b, a+b
print()

if __name__ == '__main__':main()
