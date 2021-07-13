#!/usr/bin/env python3

import platform

def main():
    print('Going to call message()')
    message()
    print('Call message() Done')

def message():
    print('The python version is {}'.format(platform.python_version()))
    if False:
        print('In side if')
    else:
        print('In side else')
    x = 42
    print('x  value = {}'.format(x))
    print(f'x  value = {x}')

print('All code done')

# Below line inform to intrpeter to check all code before executing any script
if __name__ == '__main__':main()
