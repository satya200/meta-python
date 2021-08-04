
import logging
import sys
logging.basicConfig(level=logging.DEBUG, filename="mylog.log",
                format="%(asctime)s : %(name)s : %(levelname)s : %(message)s : %(filename)s : %(lineno)d")

inv = 1
num = 5

try:
    inv = 1 / num
except ZeroDivisionError as z:
    logging.debug(z)
except TypeError as t:
    logging.warning(t)
except Exception as e:
    logging.error(e)
else:
    print(f"inverse of {num} is :{inv}")
    logging.info(f"inverse of {num} is :{inv}")
finally:
    print("Finally block of code executed.....")

# print(help("modules"))
