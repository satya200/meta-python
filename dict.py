#!/usr/bin/env python3

def main():
    # We can use below dict constructer as well
    animals = dict(kitten = 'meow', puppy = 'ruff', lion = 'grrr')
    # BElow and above both are same
    #animals = {'kitten': 'meow', 'puppy': 'ruff', 'lion': 'grrr'}
    print_dict(animals)

def print_dict(data):
    for x in data:
        print(f'{x}:{data[x]}')
    for i in data.keys():
        print(i)

if __name__ == '__main__':main()
