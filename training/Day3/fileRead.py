
FL = open("data.txt", "r")

# st = FL.read(100)

# st = FL.readline(100)
# print(st)

st = FL.readlines(1800)
print(st)
FL.close()
