
s = set()
print(s)
print(type(s))

print("-" * 40)
s1 = {1, 2, 3, 4, "five", "six"}
print(f"s1 :{s1}")
print(type(s1))

s1.add(7)
print(f"s1 :{s1}")

s1.update([7, 8, 9, 10])
print(f"s1 :{s1}")

res = s1.discard(10)
print(f"s1 :{s1}")
print(res)

res = s1.remove(8)
print(f"s1 :{s1}")
print(res)

# discard never throws an error if the specified number is not present in the set
# remove raises an keyerror exception if the specified number is not present in the set
# s1.discard(10)
# s1.remove(10)

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}
print(f"A :{A}")
print(f"B :{B}")

print("A Union B :", A | B)
print("B Union A :", B.union(A))

print("-" * 40)
print("A Intersection B :", A & B)
print("B Intersection A :", B.intersection(A))

print("-" * 40)
print("A Difference B :", A - B)
print("B Difference A :", B.difference(A))

print("-" * 40)
print("A Symmetric Difference B :", A ^ B)
print("B Symmetric Difference A :", B.symmetric_difference(A))
