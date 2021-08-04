
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"name is {self.name} and salary is {self.salary}"

    def __eq__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

emp1 = Employee("Jack", 45000)
print(emp1)

emp2 = Employee("Jill", 40000)
print(emp2)
print("-" * 40)

# comparing the addresses by default
# if we over load == operator then it overloads != also
if (emp1 != emp2):
    print("Salary NOT equal {0} and {1}".format(emp1.salary, emp2.salary))
else:
    print("Salary equal {0} and {1}".format(emp1.salary, emp2.salary))

if emp1 < emp2:
    print("{2} {0} is less than {3} {1}".format(emp1.salary, emp2.salary, emp1.name, emp2.name))
else:
    print("{3} {1} is less than {2} {0}".format(emp1.salary, emp2.salary, emp1.name, emp2.name))



