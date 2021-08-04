
import re

dt = "31/12/2021"

res = re.search(r'([0-2][1-9]|[1-3][0-1])(/|-)(0[1-9]|1[0-2])(\2)'
                r'(19[0-9]{2}|[2-9][0-9]{3})', dt)

if res:
    print("Match found...")
    print(res.group(0))
    print(res.group(1))
    print(res.group(2))
    print(res.group(3))
    print(res.group(4))
    print(res.group(5))
else:
    print("Match not found...")