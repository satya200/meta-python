
class tooYoung(Exception):
    pass

class tooOld(Exception):
    pass

age = 65

try:
    if age < 18:
        raise tooYoung("The person is too young to receive a vaccine")
    elif age >= 100:
        raise tooOld("the person is too old to receive a vaccine")
except tooYoung as y:
    print(y)
except tooOld as o:
    print(o)
else:
    print("You can receive the 1st or 2nd dose of vaccine")
finally:
    print("The vaccine process is completed...")