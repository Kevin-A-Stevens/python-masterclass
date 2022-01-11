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

