# Functional Programming
# Separation of concerns
# Separating into separate chunks
# OOP has classes, functional programming separate data and functions

from functools import reduce
from time import time

## Pure functions
# 2 rules
# 1. Given the same input = same output
# 2. A function should not produce any side effects

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))  # Same output and no side effect
# No side effect means it does not touch anything outside
# if return print(new_list) does have a side effect so would not be pure
# If new_list = [] outside the function, then that also affects the outside
# Try to create mostly pure functions

# Useful functions (map, filter, zip, reduce)
# map allows us to simplify the code we have

# map(action, [1,2,3])
def multiply_by3(item):
    return item*3

print(map(multiply_by3, [1,2,3]))  # <map object at 0x7f69a7a47040>
print(list(map(multiply_by3, [1,2,3])))

# filter
def check_odd(number):
    return number % 2 != 0

print(list(filter(check_odd, [1,2,3])))  # [1,3]

# zip - zip items together
my_list = [1,2,3]
your_list = [4,5,6]
their_list = [10,20,30]
print(list(zip(my_list, your_list, their_list))) # [(1, 4), (2, 5), (3, 6)]
print(my_list) # [1, 2, 3]

# reduce - must be imported. See above
def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0)) # 6

# Lambda expressions = one time anonymous functions
# lambda param: action(parameter)

my_list = [7,8,9]
print(list(map(lambda item: item*4, my_list))) # [28, 32, 36]
print(list(filter(lambda item: item % 2 != 0, my_list))) # [7,9]
print(reduce(lambda acc, item: acc + item, my_list)) # 24

my_list = [5,4,3]
new_list = list(map(lambda item: item**2, my_list))
print(new_list) # [25, 16, 9]

# list sorting

a = [(0,2), (4,3), (10,-1), (9,9)]
a.sort(key=lambda x: x[1])
print(a)

# List Comprehensions - quick way to create a list
# my_list = [var for var in iterable]
my_list = [char for char in "hello"]
print(my_list)

my_list2 = [num for num in range(0,30)]
print(my_list2)

my_list3 = [num * 2 for num in range(0,11)]
print(my_list3)

my_list4 = [num**2 for num in range(0,100) if num % 2 == 0] # All even numbers
print(my_list4)

my_list5 = [num**2 for num in range(0,100) if num % 2 != 0] # All odd numbers
print(my_list5)

# Set and dictionary comprehensions
my_list = {char for char in "kevin"}
print(my_list)

simple_dict = {
    "a": 1,
    "b": 2
}
my_dict = {k:v**2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict)

my_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)

some_list = ["a", "b", "c", "b", "d", "n", "m", "n"]
duplicates = {x for x in some_list if some_list.count(x) > 1}
print(duplicates)

# Decorators - supercharge our functions

def my_decorator(func): # accepting a function
    def wrap_func(): # wrapping a function
        print("********")
        func() # calling a function
        print("********")
    return wrap_func # returning a wrapper function

@my_decorator
def hello():
    print("Hello")

@my_decorator
def bye():
    print("See ya later")

hello()
bye()

def my_decorator2(func2): # accepting a function
    def wrap_func(*args, **kwargs): # wrapping a function
        print("********")
        func2(*args, **kwargs) # calling a function
        print("********")
    return wrap_func # returning a wrapper function

@my_decorator2
def hello2(greeting, emoji=":)"):
    print(greeting, emoji)

hello2("Hi")

# Measure time it takes to run a function

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2 - t1} ms")
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000000):
        i*5

long_time()







