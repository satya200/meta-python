
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['Java', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJS']

    def __str__(self):
        return f"name is {self.name} and salary is {self.salary}"

    def __len__(self):
        return len(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __iter__(self):
        return iter(self.tech)

    def __getitem__(self, index):
        return  self.tech[index]

    def __setitem__(self, index, val):
        self.tech[index] = val

emp1 = Employee("Jack", 45000)
emp1.append("Python")

print([t for t in emp1])
print("-" * 40)

a = emp1[2]
print(a)

print("-" * 40)
emp1[5] = 'NodeJS'
print([t for t in emp1])