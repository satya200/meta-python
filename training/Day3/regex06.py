
import re

str = """the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
"""

reg = re.compile(r'(t\w+)')
res = re.findall(reg, str)
print(res)
print("Total words :", res.count('the'))
