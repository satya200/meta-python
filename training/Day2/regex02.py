
import re
# res = re.search(r'(\w+)', st)
# res = re.search(r'(\W+)', st)
# res = re.search(r'(\d+)', st)
# res = re.search(r'(\D+)', st)
# res = re.search(r'(\s+)', st)
# res = re.search(r'(\S+)', st)


st = "This is a sample aMple string"

res = re.search(r'(\ba\w+)', st)

if res:
    print("Match Found....")
    print(res.group(0))
else:
    print("Match not Found....")
