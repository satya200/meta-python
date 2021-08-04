
from collections import namedtuple
# collection is the name of a module and we are importing namedtuple class


def greet():
    print("Hello Mr. Jack Welcome to the training")

def greetGst(gname):
    print(f"Hello Mr. {gname} Welcome to the training")

# default args
def greetGstcity(gname, city="Chennai"):
    print(f"Hello Mr. {gname} from {city}, Welcome to the training")

greet()
greetGst("Mike")
greetGstcity("Jane")
greetGstcity("Ram")
greetGstcity("Amit", "Bangalore")

print("-" * 40)
def add(x, y):
    return x + y

print("The sum of %d, %d is :%d" % (15, 18, add(15, 18)))

def ArithematicCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

print(ArithematicCalc(20, 5))

print("-" * 40)
def BasicArithematic(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    # create a named tuple
    result = namedtuple("Result", "sum prod diff quot")
    current_result = result(sum=sum, prod=prod, diff=diff, quot=quot)
    print(current_result.sum)
    return current_result

print(BasicArithematic(20, 4))
res = BasicArithematic(20, 4)
print("Sum :", res.sum)
print("Diff :", res.diff)
print("Prod :", res.prod)
print("Quot :", res.quot)

# Variable length arguments
# list, dictionary (*args, **kwargs)
print("-" * 40)
def CntryCities(cntry, *cities):
    print(f"Country :{cntry}")
    print(cities)
    print(*cities)       # unpacking

CntryCities("India", "Delhi", "Mumbai", "Chennai", "Kolkotta")

print("-" * 40)
def CntryTemp(cntry, **temp):
    print(f"Country :{cntry}")
    print(temp)

ctry = input("Enter the country name :")

CntryTemp("Inida", Delhi=24.5, Mumbai=20.1, Chennai=28.7, Kolkotta=26.9)
