#!/usr/bin/env python3

# Below is defination of class
class Duck:
    sound = 'Quaaaackk!'
    def quack(self):
        print('Quaaack!')
        print(self.sound)

    def walk(self):
        print('Walk like Duck')
        print(self.sound)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__':main()
