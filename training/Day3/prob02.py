
import re

url = "https:// www.google.com / search=“%new hindi movies? % / get_data2019 " \
      "/ fetch_data%frm_1 / imdb? %hindi%movies1995to2020$& / result = page1.aspx"

"""
1. before /
2. between /
3. after /
"""

# while(re.search(r'(//|/)', url)):
#     res = re.search(r'(//|/)', url)

while(re.search(r'(?<=\/)(.*?)(?=\/)', url)):
    res = re.search(r'(?<=\/)(.*?)(?=\/)', url)
    print(url[res.start():res.end()])
    url = url[res.end():]

# print(url)

