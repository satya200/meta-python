
def callMe():
    print(f"Apples from Ooty...")

def fun(fnc):
    print("Hello....")
    fnc()
    print("Hi....")
    print("-" * 40)

    def defineMe():
        print(f"Oranges from Nagpur...")

    return defineMe

def funCallback(fnc):
    print("India is great....")
    fnc()
    print("Mera Bharath Mahan...")

funCallback(fun(callMe))
