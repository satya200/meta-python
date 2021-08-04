
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def __disp(self):
        print("Private Method...")

    def __str__(self):
        return f"name is  {self.name} and salary is {self.__salary}"

    def callPrivate(self):
        self.__disp()


emp = Employee("Mike", 50000)
print(emp)

print(emp.name)
print(emp.__dict__)
print(emp._Employee__salary)
