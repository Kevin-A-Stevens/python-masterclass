# Data Types
"""
int
float
bool
str
list
tuple
set
dict
"""

# Classes -> custom types = Create our own

# Specialized Data Types = Modules

# Fundamental Data Types

# type action/function
print(type(2 + 4)) # prints out the data type   <class 'int'>
print(type(2 - 4)) # <class 'int'>
print(type(2 * 4)) # <class 'int'>

# float
print(type(2 / 4)) # <class 'float'>
print(type(0.00001)) # <class 'float'>
print(type(20 + 1.1)) # expression is converted into a float

print(2 ** 3) # powers
print(5 // 4) # // rounds down to an integer
print(5 % 4) # prints remainder of the division

# round action/function
print(round(3.1)) # round to nearest int

# abs = returns absolute value
print(abs(-20))

# Operator precedence
"""
()
**
* and /
+ and -
"""

# Complex data type
"""
Only used for really complex math
"""

# bin action/functions gives the binary representation
print(bin(5))  # 0b101  where 101 in binary for 5

# int action/function converts binary to integer. 2 means base 2 (binary)
print(int("0b101", 2))

# Variables

iq = 190
print(iq)

"""
snake_case
start with a lowercase or _
letters, numbers, underscores
case sensitive
don't over-write keywords
"""

user_iq = 190
_user_iq = 190
user4_iq = 200

# Constants = a variable that will not change
# All caps tell a programmer that this is a constant and does not change
PI = 3.14

# dunder variables are meant to be left alone
# __file__

# A quick way to assign variables
a,b,c = 1,2,3
print(a)
print(b)
print(c)

# Augmented assignment operator
some_value = 5
some_value += 2
print(some_value)

# str
print(type("Hey there!")) # <class 'str'>
long_string = '''
WOW
0 0
---
'''
print(long_string)
first_name = "Kevin"
last_name = "stevens"
full_name = first_name + " " + last_name
print(full_name)

# string concatenation
print("Hello" + " Kevin")

# Type Conversion = converting the type of your Data Type
print(type(str(100))) # <class 'str'>
print(type(int(str(100)))) # <class 'int'>

# Escape Sequence
weather = "\tIt's \"kind of\" Sunny \n Hope you have a great day"
print(weather)

# Formatted Strings
age = 44
name = 'Johnny'
print(f"Hi {name}, you are {age} years old")
print("Hi {0}, you are {1} years old".format(name, age))

# String Indexes [start:stop:step]
self = "01234567"
print(self[0])  # 0
print(self[0:2]) # 01
print(self[0:8])
print(self[0:8:2])
print(self[0:])
print(self[:5])
print(self[-1])
print(self[::-1])   # Reverse a string

# Immutability
# Cannot change part of a string.
# self[0] = 8
# Strings are immutable. Have to change the whole string or create a new variable

# Built-in Functions and Methods
# len()

print(len("Hello"))  # prints length of a string
greet = "Hello"
print(greet[0:len(greet)])

# String Methods
quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find("be"))
print(quote.replace("be", "me"))
print(quote)

# Booleans = True or False
my_name = "Kevin"
is_cool = True
print(type(is_cool))  # <class 'bool'>

current_year = 2022
birth_year = input("What year were you born? ")
age = current_year - int(birth_year)
print(f"Your age is: {age}")









