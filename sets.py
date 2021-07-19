#!/usr/bin/env python3

def main():
    a = set(" we afre gone negative.")
    b = set("I am sorry aski")
    print_set(a)
    print_set(b)

def print_set(output):
    print('{',end = '')
    for x in output: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
