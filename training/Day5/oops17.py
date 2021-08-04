
class Animal:

    def __init__(self):
        print("Animal Ctor")
        self.age = 1

    def eat(self):
        print("Animals Eat...")

# inheritance
class Bird(Animal):

    def __init__(self):     # overriding parent class ctor
        super().__init__()
        self.size = "1k"
        print("Bird Ctor")

    def fly(self):
        print("Birds Fly...")

parrot = Bird()
print(parrot.__dict__)
print(parrot.age)
print(parrot.size)
