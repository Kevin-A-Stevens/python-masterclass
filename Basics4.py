# Functions
def say_hello(name="Darth Vader", emoji=":)"):
    print(f"Hello {name} {emoji}")

# positional argument = better practice
say_hello("Kevin", ":)")

# keyword argument
say_hello(name="Bibi", emoji=":)")

say_hello() # uses default parameters defined in the function

# function can do two things.
# returns something
# modifies something
# a function should do one thing really well
# usually a function should return something
# return exits the function

def sum(num1, num2):
    return num1 + num2

total = sum(12,4) # Can assign a variable because the function returns it
print(sum(10,5)) # prints None so need to return the answer
print(total)

# Methods vs Functions
"""
Functions
list()
print()
max()
min()
input()
def some_function()

Methods = built in objects that have methods
use them using dot notation
"Hello".method
"""

# docstrings = use single quotes. See by hovering over test()
def test(a):
    '''
    Info: This function tests and prints param, a
    '''
    print(a)
test(5)

help(test) # use help to see docstring
print(test.__doc__) # use .__doc__ to see docstring

# clean code
# odd or even

def is_even(num):
    return num % 2 == 0

print(is_even(50))



