#!/usr/bin/env python3

# This file is same as class1.py but some more good coding style

class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten' # defalult value assign if not present
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rawr'

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound
    # Below is special type of method use for print. When we call print below methode ll invoke
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}"'

#def print_animal(obj):
#    if not isinstance(obj, Animal):
#        raise TypeError('print_animal(): Requires an Animal')
#    print('The {} is named "{}" and says "{}".'.format(obj.type(), obj.name(), obj.sound()))

def main():
    a0 = Animal(type='Kitten', name='fluffy', sound='rawr')
    a1 = Animal(type='duck', name='donald', sound='quack')
    print(a0)
    print(a1)
    #print_animal(Animal(type='Satya', name='Sundar', sound='Sahu'))

if __name__ == '__main__': main()
