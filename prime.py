#!/usr/bin/env python3

def main():
    if isprime(num):
        print('{} is prime'.format(num))
    else:
        print(f'{num} is not prime')

def isprime(num):
    if num <= 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

num = 6

if __name__ == '__main__':main()
