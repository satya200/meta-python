
FL = open("data.txt", "rb")

print(FL.tell())

pos = FL.seek(100, 0)
print(pos)

pos = FL.seek(80, 1)
print(pos)

pos = FL.seek(100, 2)
print(pos)   # 4366 + 100 = 4466

pos = FL.seek(-100, 2)
print(pos)  # 4366 - 100 = 4266

# pos = FL.seek(-50, 0)
# print(pos)

FL.close()