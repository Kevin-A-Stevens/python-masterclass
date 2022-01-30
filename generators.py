# Generators: Allow us to generate a sequence of value over time
# range(100) is a generator

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result
#
# my_list = make_list(100) # my_list creates a list in memory
# print(my_list)

from time import time
# range does not create a list in memory. It never creates the list like the above does

def generator_function(num):
    for i in range(num):
        yield i  # yield pauses the function and comes back when next is called

for item in generator_function(1000):
    print(item)

# Notice is kept going one by one without storing all items in memory

g = generator_function(100)
print(g)  # <generator object generator_function at 0x7f96f20cbdd0>

print(next(g))
print(next(g))
print(next(g))
print(next(g))

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
    print("1")
    for i in range(10000000):
        i*5

@performance
def long_time2():
    print("2")
    for i in list(range(10000000)):
        i*5

long_time() # faster
long_time2() # slower

# Fibonacci Numbers
# Generator
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(20):
    print(x)

# List
def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2(20))

