
FW = open("myfile.txt", "w")

# st = input("Enter the contents of the file :")

l1 = "this is the first line. \n"
l2 = "this is the second line. \n"
l3 = "this is the third line. \n"

# FW.write(st)

FW.writelines([l1, l2, l3])

FW.close()