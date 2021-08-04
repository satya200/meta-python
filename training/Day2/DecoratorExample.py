
import time
def timecalc(fnc):

    def helperFun(i):
        strTime = time.time()
        fnc(i)
        endTime = time.time()
        print(f"The time taken by {fnc.__name__} to execute is {endTime - strTime}")

    return helperFun


