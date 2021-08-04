"""
a. count of males and females
b. unique list of desig
c. unique list of dept
d. sum of all salaries
"""

gender = {}
desig = []
dept = []
sal = 0

FL = open("EMP.csv", "r")

for line in FL.readlines():

    g = line.split(",")[2]
    ds = line.split(",")[3]
    dp = line.split(",")[4]

    if g not in gender:
        gender[g] = 1
    else:
        gender[g] += 1

    if ds not in desig:
        desig.append(ds)

    if dp not in dept:
        dept.append(dp)

    sal += int(line.split(",")[5])

FL.close()

print(gender)
print(desig)
print(dept)
print(sal)
