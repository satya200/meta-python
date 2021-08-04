#!/usr/bin/env python3

def main():
    try:
        #x = int('foo')
        x = 5/3
    except ValueError:
        print('I am Satya Sunda')
    except ZeroDivisionError:
        print('Do not divide by zero')
    except:
        print('Unknown error')
    else:
        print('Good Job')
        print(x)

if __name__ == '__main__': main()
