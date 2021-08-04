
import re

str = "good blood bad blood"

res = re.search(r'(\w+)(\s)(\w+)\s(\w+)\s(\3)', str)

if res:
    print("Match found...")
    print(res.group(0))
    print(res.group(0))
    print(res.group(1))
    print(res.group(2))
    print(res.group(3))
    print(res.group(4))
    print(res.group(5))
else:
    print("Match not found...")