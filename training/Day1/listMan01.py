#!/usr/bin/env python3

l = list()
print(l)
print(type(l))

l = (1, "Hello", 3, 4, 5)
#l = (1, 2, 3, 4, 5)
print(f"the values of l is :{l}")

print(id(l[0]))
print(id(l[1]))
print(id(l[2]))

l = list(range(1, 10))
print(l)

print("-" * 40)

print(l)
print(l[4])
print(l[0:5])

print(l[-1])
print(l[-1:-6:-1])

print(l[:])
print(l[::-1])

# print(dir(l))

# shallow copy
print("-" * 40)
l1 = list(range(1, 11))
print(f"list l1 before :{l1}")
l2 = l1
print(f"list l2 before :{l2}")

print("-" * 40)
l1.insert(5, [100, 200, 300])
print(f"list l1 after :{l1}")
print(f"list l2 after :{l2}")

# Deep Copy
print("Deep Copy".center(40, "-"))
l3 = list(range(10, 101, 10))
print(f"list l3 before :{l3}")
l4 = l3.copy()
print(f"list l4 before :{l4}")
print("-" * 40)
l3.insert(3, [5, 10, 15, 20])
print(f"list l3 after :{l3}")
print(f"list l4 after :{l4}")


print("Two dimensional array".center(50, "-"))
tda1 = [[1, 2, 3], [4, 5, 6]]
print(f"list tda1 before :{tda1}")
tda2 = tda1.copy()
print(f"list tda2 before :{tda2}")

print("-" * 40)
print(tda1[1][1])
tda1[1][1] = 555
print(f"list tda1 after :{tda1}")
print(f"list tda2 after :{tda2}")

print("-" * 40)
print(f"tda1 :{id(tda1[1][1])}")
print(f"tda2 :{id(tda2[1][1])}")

import copy

print("solution".center(40, "-"))
tda3 = [[10, 20, 30], [40, 50, 60]]
print(f"list tda3 before :{tda3}")
tda4 = copy.deepcopy(tda3)
print(f"list tda4 before :{tda4}")

print("-" * 40)
print(tda3[1][1])
tda3[1][1] = 999
print(f"list tda3 after :{tda3}")
print(f"list tda4 after :{tda4}")

print("-" * 40)
print(f"tda1 :{id(tda3[1][1])}")
print(f"tda2 :{id(tda4[1][1])}")
