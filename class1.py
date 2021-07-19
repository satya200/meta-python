#!/usr/bin/env python3

class Animal:
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(obj):
    if not isinstance(obj, Animal):
        raise TypeError('print_animal(): Requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(obj.type(), obj.name(), obj.sound()))

def main():
    a0 = Animal('Kitten', 'fluffy', 'rawr')
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('Satya', 'Sundar', 'Sahu'))

if __name__ == '__main__': main()
