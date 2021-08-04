#!/usr/bin/env python3

#s1={1, 2, 3}
#s2={4, 5, 6}
#print(s1.isdisjoint(s2))
#print(s2.isdisjoint(s1))

s1={3,4}
s2={1,2}
s3=set()
i=0
j=0
for i in s1:
    for j in s2:
        s3.add((i,j))
        i+=1
        j+=1
print(s3)

#def test(i,j):
#    if (i==0):
#        return j
#    else:
#        return test(i-1,i+j)
#print(test(4,7))

#def fact(num):
#    if num == 0:
#        return 1
#    else:
#        return num*fact(num-1)
#print(fact(3))

#def foo(x):
#    x[0] = ['def'] 
#    x[1] = ['abc'] 
#    return id(x)
#q = ['abc', 'def']
#print(id(q) == foo(q))

#def find(a, **b):
#    print(type(b))
#find('letters',A='1',B='2')

#a=10
#b=20
#def change():
#    global b
#    a=45
#    b=56
#change()
#print(a)
#print(b)

#cnt={}
#cnt[(1,2,4)] = 5
#cnt[(4,2,1)] = 7
#cnt[(1,2)] = 6
#cnt[(4,2,1)] = 2
#tot = 0
#for i in cnt:
#    tot=tot+cnt[i]
#print(len(cnt)+tot) #16

#A = [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]
#print(A[1])

#my_string = "hellow world"
#k = [(i.upper(), len(i)) for i in my_string]
#print(k)

#my_string = "Sa@tya"
#k = [print(i) for i in my_string if i not in "aeiou"]

class parent:
    def __init__(self, param):
        self.v1 = param
class child(parent):
    def __init__(self, param):
        self.v2 = param
obj = child(11)
print("%d %d" % (obj.v1, obj.v2)) # Error

#def myfunc(x, y, z, a):
#    print(x + y)
#num = [1, 2, 3, 4]
#myfunc(*num)

#def add(listpa):
#    listpa += [1]
#mylist = [1, 2, 3, 4]
#add(mylist)
#print(len(mylist))
#print(mylist)

#for i in range(2):
#    print(i)
#for i in range(4, 6):
#    print(i)

#import re
#sum = 0
#pattern = 'back'
#if re.match(pattern, backup.txt):
#    sum += 1
#if re.match(pattern, text.back):
#    sum += 2
#if re.match(pattern, backup.txt):
#    sum += 4
#if re.match(pattern, text.back):
#    sum += 8
#print('sum')

#class Acnt:
#    def __init__(self, id):
#        self.id = id
#        id = 666
#acc = Acnt(123)
#print(acc.id)

#name = "snow storm"
#print("%s" % name[6:8])

#print("\x48\x49!")

#f = None
#for i in range (5):
#    with open("data.txt","w") as f:
#        if i > 2:
#            break
#print(f.closed)

#d = lambda p: p * 2
#t = lambda p: p * 3
#x = 2
#x = d(x)
#x = t(x)
#x = d(x)
#print(x)

#a = [1,2,3,None,(),[],]
#print(len(a))

#def f(): pass

#print(type(f()))

#def main():
#    a(1,2,3)

#if __name__ == '__main__':main()
