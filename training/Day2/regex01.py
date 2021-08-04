"""
display all the modules available to be imported...
# print(help("modules"))

"""

import re

# res = re.match(r'^hello', st, re.I)   # re.I means Ignore case and it is called as modifier
# res = re.search(r'World$', st) # st = "Hello World"
# res = re.search(r'b.t', st)
# res = re.search(r'ba*t', st)
# res = re.search(r'ba+t', st)
# res = re.search(r'ba{3}t', st)
# res = re.search(r'ba{3,}t', st)
# res = re.search(r'ba{3,7}t', st)
# res = re.search(r'b[a-zA-Z0-9]t', st)
# res = re.search(r'b[aeiou]t', st)
# res = re.search(r'b[^aeiou]t', st)
# res = re.search(r'b(ai|oa)t', st)


st = "sample.txt"

res = re.search(r'\.txt$', st)

print(res)

if res:
    print("Match found...")
    print(res.group(0))
else:
    print("Match not found....")