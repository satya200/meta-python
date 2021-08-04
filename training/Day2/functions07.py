
def add(x, y):
    print("Add called....")
    return x + y

def sub(x, y):
    print("Sub called.....")
    return x - y

def outerFun(fnc):

    def helperFun(x, y):
        print("Logging into the service.....")
        print(fnc(x, y))
        print("Logging out of the service....")

    return helperFun


addFun = outerFun(add)
addFun(10, 20)
