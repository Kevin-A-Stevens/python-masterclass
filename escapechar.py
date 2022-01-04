# \n prints a new line
splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

# \t prints a tab
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# The \ can also be used to escape characters
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')

# can also use """ and no need to use escape character
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

anotherSplitString = """This string has been
split over
several
lines"""

print(anotherSplitString)

# include the \ character
print("C:\\Users\\kstevens\\notes.txt") # preferable
print(r"C:\Users:\kstevens\notes.txt")

age = 24

# checking variable type
print(type(age))
print(type(anotherSplitString))

# concatenate strings and integers
# str converts age to a string
print("Your age is " + str(age) + " years old")

# Data types
# int = have no fractional part. No maximum size
# float = have a fractional part
# floats have 52 digit precision
# If you need more precision, Python 3 has Decimal data type


