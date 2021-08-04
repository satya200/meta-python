#!/usr/nin/env python3

t1 = tuple()
print(t1)
print(type(t1))

print("-" * 40)
t2 = (1, 2, 3, 4, 5)
print(t2)
print(type(t2))

print("-" * 40)
t3 = tuple(range(1, 11))
print(t3)
print(type(t3))

print("-" * 40)
t4 = 10,
t5 = 10, 20, 30

print(f"t4 :{t4} {type(t4)}")
print(f"t5 :{t5} {type(t5)}")

print("-" * 40)
t = tuple(range(1, 6))
print(t)
print(t[0])
print(t[3])
print(t[0:3])

print(t[-1])
print(t[-4])
print(t[-1:-4:-1])

# print(t[3])
# t[3] = 44
# print(t)

for i in t:
    print(i, end=" ")
print("\n")
