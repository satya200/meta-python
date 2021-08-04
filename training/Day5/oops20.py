
from abc import ABC, abstractmethod

# Abstract class
class Bank(ABC):
    @abstractmethod
    def doJob(self):
        pass

class Manager(Bank):
    def doJob(self):
        print("Manager Job....")

class Cashier(Bank):
    def doJob(self):
        print("Cashier Job...")


def BankFun(emp):
    print("BankjobStarted".center(40, "-"))
    emp.doJob()
    print("BankjobCompleted".center(40, "-"))
    print("-" * 40)

Mike = Manager()
Charles = Cashier()

BankFun(Mike)
BankFun(Charles)


