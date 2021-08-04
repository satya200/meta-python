
from DecoratorExample import timecalc
import sys

@timecalc
def calcFun(max):
    print("calcFun called......")
    lst = []
    for i in range(1, max):
        for j in range(1, i+1):
            lst.append(j)

calcFun(7000)

print(sys.path)