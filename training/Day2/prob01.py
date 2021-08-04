
import re

lno = "LCNO-TND-15-2021-025"

res = re.search(r'LCNO-()-()-()-()', lno)

if res:
    print("Match found...")
    print(res.group(0))
else:
    print("Match not found....")