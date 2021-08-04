class lenExcetion(Exception):
    pass
class contentException(Exception):
    pass

l1 = [1, 2]
l2 = [2, 3]

try:
    if(len(l1) != len(l2)):
        raise lenExcetion("Length are not equal")
    if l1 != l2:
        raise contentException("Contents are not same")
except lenExcetion as le:
    print(le)
except contentException as ce:
    print(ce)
else:
    print("lists are equal")
finally:
    print("done")