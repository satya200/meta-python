"""
rejected string - "the quick brown fox"
matched string - "jumps"
unchecked string - "over the lazy dog"
"""
import re

str = "the quick brown fox jumps over the lazy dog"

res = re.search(r'(j\w+)', str)

if res:
    print("Match found...")
    print("Rejected String  :", str[:res.start()])
    print("Matched String   :", res.group(0))
    print("Unchecked String :", str[res.end():])
else:
    print("Match not found...")