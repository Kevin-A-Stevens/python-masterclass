#import utility
# import shopping.more_shopping.shopping_cart
from utility import multiply, divide
from shopping.more_shopping.shopping_cart import buy
import random  # built-in module in Python
import sys  # built-in module in Python

#print(utility.multiply(2,3))
print(multiply(2,3))
print(divide(6,3))
# <module 'utility' from '/home/kevinstevens/Documents/Development/Python/python-masterclass/utility.py'>

# print(shopping.more_shopping.shopping_cart)
# <module 'shopping.shopping_cart' from '/home/kevinstevens/Documents/Development/Python/python-masterclass/shopping/shopping_cart.py'>

# print(shopping.more_shopping.shopping_cart.buy("apple"))
print(buy("apple"))

# new python package creates a new folder
# package has an __init__.py file at the root

print(max([1,2,3]))

print(__name__)  # __main__
# __name__
if __name__ == "__main__":  # Only run if this is the main file
    print("Please run this")

help(random)  # help page for the module
print(dir(random))  # shows all the methods useable for this module

print(random.random()) # random number between 0 and 1
print(random.randint(1, 10)) # random int between 1 and 10
print(random.choice([1,2,3,4,5])) # chooses one from the list given

my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)

# first = sys.argv[1]
# second = sys.argv[2]
# print(f"Hello {first} {last}")

# Useful Modules

# Counter keeps track of how many times and item occurred. Creates a dictionary.
from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]  # Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
print(Counter(li))
sentence = "blah blah blah thinking about python"
print(Counter(sentence))

# defaultdict allows you to search a key and get 0 if it doesn't exist
dictionary = defaultdict(int, {"a": 1, "b": 2})
print(dictionary["c"])

d = OrderedDict()
d["A"] = 1
d["B"] = 2

d2 = OrderedDict()
d2["A"] = 1
d2["B"] = 2

print(d2 == d)

d3 = OrderedDict() # looks at order of items
d3["A"] = 2
d3["B"] = 1

print(d2 == d3)

"""
Recently, the Python has made Dictionaries ordered by default! 
So unless you need to maintain older version of Python 
(older than 3.7), you no longer need to use ordered dict, 
you can just use regular dictionaries!
"""

# Datetime module

import datetime

print(datetime.time())  # 00:00:00
print(datetime.time(5,45,2))  # 05:45:02
print(datetime.date.today())  # 2022-01-31

# array package and array module
from array import array

arr = array("i", [1,2,3]) # "i" = integer
print(arr[0])  # Can access it like a list and has better performance









