
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['Java', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJS']

    def __str__(self):
        return f"name is {self.name} and salary is {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

emp1 = Employee("Jack", 45000)
emp2 = Employee("Jill", 50000)

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 40)
print(emp1 + emp2)

print("-" * 40)
print(emp1 - emp2)

print("-" * 40)
print(emp1 * emp2)

print("-" * 40)
print(emp1 / emp2)

print("-" * 40)
print(emp1 // emp2)

print("-" * 40)
print(len(emp1))

print("-" * 40)
# iterating
# print([tec for tec in emp1])      # comprehension

for tec in emp1:
    print(tec, end=" ")
print()



