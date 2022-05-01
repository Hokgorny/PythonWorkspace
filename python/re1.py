import re

p = re.compile("ca.e") # . : 하나의 문자를 의미

m = p.match("case")
print(m.group())