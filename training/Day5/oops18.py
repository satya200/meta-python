
class Animal:

    def __init__(self):
        print("Animal Ctor")
        self.a = 200

    def eat(self):
        print("Animals Eat...")

class Human:

    def __init__(self):
        print("Human Ctor")
        self.h = 100

    def talk(self):
        print("Humans can talk....")

class Boy(Human, Animal):
    def __init__(self):
        self.b = 300
        super().__init__()
        # super().__init__()
        Animal.__init__(self)

ben = Boy()
ben.talk()
ben.eat()

print(ben.__dict__)
print(ben.b)
print(ben.h)
print(ben.a)
