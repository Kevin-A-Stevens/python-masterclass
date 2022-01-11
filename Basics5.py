# Functions continued
# *args and **kwargs
# *args = can accept any number of arguments
# **kwargs = can use any number of keyword arguments
def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs
# Usually you are using only 1 or 2 of these

# Walrus Operator := Assigns values to variables as part of a larger expression
a = "Hellooooooooooooo"
if ((n := len(a)) > 10):
    print(f"Too long {n} elements.")

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]
print(a)

# Scope = What variables do I have access to
# Global scope = anyone can use this variable anywhere

a = 1
def conf():
    a = 5
    return a
print(a)  # 1
print(conf())  # 5
print(a)  # 1

# Scope Rules
"""
1 - Start with local
2 - Parent local?
3 - Global
4 - Built in Python functions
"""

# Global keyword
"""
total = 0
def count():
    global total
    total += 1
    return total
count()
count()
print(count())
"""

# A better way is not using the global keyword
total = 0
def count(total):
    total += 1
    return total
count(total)
count(total)
print(count(count(count(total))))

# nonlocal keyword
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner", x)
    inner()
    print("outer", x)
outer()

x = float(2.8)
print(x)
