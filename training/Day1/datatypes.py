#!/usr/bin/env python3

i = 10
print(f"the value of i is :{i}")     # interpolation
print(f"variable i is :{type(i)}")

print("-" * 40)
i = "hello"
print(f"the value of i is :{i}")     # interpolation
print(f"variable i is :{type(i)}")
print(i.upper())

print(i[0])
# i[0] = "H"     => strings are immutable
print(id(i))

print("-" * 40)
i = "world"
print(id(i))

print("-" * 40)
print(len(str(2 ** 10)))

print(True)
print(False)

n = 0
while True:
    #print("Hello World \n" * 10) # This ll print hello world 10 times in each iteration
    print("Hello World \n")
    n += 1
    if n >= 10:
        break

