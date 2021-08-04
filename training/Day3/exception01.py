
import sys

num = 5
inv = 1

try:
    inv = 1 / num
# # except ZeroDivisionError as z:
# except:
#     print(sys.exc_info())
#     print(sys.exc_info()[0])
#     print(sys.exc_info()[1])
#     # print(z)
except Exception as e:
    print(e)
except ZeroDivisionError as z:
    print(z)
except NameError as n:
    print(n)
except TypeError as t:
    print(t)
else:
    print(f"The result :{inv}")
finally:
    print("finally block code...")