
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self):
        print("Account Ctor")

    @abstractmethod
    def getBalance(self):
        pass

class Savings(Account):

    def getBalance(self):
        print("prints the account balance....")

    def deposit(self):
        print("used to add money into the account.....")

class Current(Account):

    def getBalance(self):
        print("prints the account balance....")

    def transaction(self):
        print("Current account trasaction...")

# cannot create an object of abstract class
# mandatory to overide all the methods of the abstract class

s1 = Savings()
s1.deposit()

c1 = Current()
# a1 = Account()