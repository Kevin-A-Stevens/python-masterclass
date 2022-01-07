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
