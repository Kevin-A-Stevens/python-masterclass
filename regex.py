# Regular expressions

import re

email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
pattern = re.compile("this")
string = "Search this inside of this text please!"
email1 = "b@b.com"
print("Search" in string) # True
print(re.search("this", string))  # <re.Match object; span=(7, 11), match='this'>

email1_search = email_pattern.search(email1)
print(email1_search)

a = re.search("this", string)
print(a.span())  # (7, 11)
print(a.start())  # 7
print(a.end())  # 11
print(a.group())  # this

b = pattern.search(string)
print(b.group())  # this

c = pattern.findall(string)
print(c)  # ['this', 'this']

d = pattern.fullmatch(string)
print(d)  # None - must match full string

e = pattern.match(string)
print(e)






