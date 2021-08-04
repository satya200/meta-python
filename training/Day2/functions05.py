

def outerFun(greet):

    def innerFun(gname):
        print(greet, gname)

    return innerFun

greetFun = outerFun("Welcome")
spnshGreet = outerFun("Hola")
tamilGreet = outerFun("Vannakam")

# simple curry
greetFun("Sachin")
spnshGreet("Messi")       # spanish
tamilGreet("Dhoni")