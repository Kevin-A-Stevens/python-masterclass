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




