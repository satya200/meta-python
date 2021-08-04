
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
# match is a variable
for match in re.finditer(reg, str):
    st = match.start()
    en = match.end()
    print("Found '%s' at index %d %d" % (str[st:en], st, en))
