import re

# At least 8 characters long
# contain any sort letters, numbers, $%#@
# must end with a number

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password = "sgfdsaf$#1dsfd4"
check = pattern.fullmatch(password)
print(check)  # <re.Match object; span=(0, 15), match='sgfdsaf$#1dsfd4'>

