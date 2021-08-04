
# closure
def outerFun():   # Higher Order Function (HOF)
    str = "Hello World"

    def innerFun():
        print(str)

    return innerFun

outerFun()()
print("-" * 40)
print(outerFun.__name__)
print(outerFun().__name__)

print("-" * 40)
res = outerFun()
print(res)
res()
