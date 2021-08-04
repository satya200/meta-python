
class Animal:

    def __init__(self):
        print("Animal Ctor")
        self.age = 1

    def eat(self):
        print("Animals Eat...")

# inheritance
class Bird(Animal):

    def fly(self):
        print("Birds Fly...")

class Fish(Animal):

    def swim(self):
        print("fishes swim...")

cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()
print("-" * 40)

shark = Fish()
shark.swim()
shark.eat()

print(cuckoo.__dict__)
print(shark.__dict__)

print("-" * 40)
print(isinstance(cuckoo, Bird))
print(isinstance(cuckoo, Animal))
print(isinstance(cuckoo, object))

print("-" * 40)
print(issubclass(Bird, Animal))
print(issubclass(Bird, object))
print(issubclass(Bird, Fish))
