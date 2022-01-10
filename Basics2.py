# Lists = An ordered sequence of objects that can be any type
# A list is a form of array
# Lists are mutable
li = [1, 2, 3, 4, 5]
li2 = ["a", "b", "c"]
li3 = [1, 2, "a", True]

# Data Structure = A way for us to organize information into a folder or container

amazon_cart = [
    "notebooks",
    "sunglasses",
    "toys",
    "grapes"
]
print(amazon_cart[0])

# List Slicing
print(amazon_cart[0:2]) # ['notebooks', 'sunglasses']
print(amazon_cart[0::2]) # ['notebooks', 'toys']

# Lists are mutable
amazon_cart[0] = "laptop"
print(amazon_cart)
print(amazon_cart[1:3])  # ['sunglasses', 'toys']

# Matrix - A way to describe 2d lists
# Matrix is common in Machine Learning and Image Processing
matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
]

print(matrix[0][1])  # 2

# List Methods
basket = [1,2,3,4,5]
basket.append(100)  # Add an item to the end
print(basket)

basket.insert(4, 101)  # Insert into a list at a certain index
print(basket)

basket.extend([102, 103]) # Extends a list
print(basket)

basket.pop()  # Removes last item in a list and returns that value
print(basket)

basket.pop(0) # removes an item at that index
print(basket)

basket.remove(4)  # Removes a certain value
print(basket)

basket.clear() # Clears what is in the list
print(basket)

basket = [6,8,7,9,10]
print(basket)
print(basket.index(7)) # Get index number of a value
print(basket.index(8, 0, 3)) # start and stop search at specific index numbers
print(9 in basket) # True of False if an item is in a list or not
print(basket.count(10))  # Prints how many times the item occurs
basket.sort() # sorts items in a list
print(basket)
print(sorted(basket))  # sorts and produces a new copy and sorts it
another_basket = basket.copy() # Copies the list
print(another_basket)
basket.reverse()
print(basket) # Reverses the list in place
# To sort a list in reverse order
basket = [8,5,2,9,1]
print(basket)
basket.sort()
basket.reverse()
print(basket)

# Common List Patterns
my_basket = ["socks", "shirts", "pants", "shorts", "gloves", "books"]
print(my_basket)
print(my_basket[::-1]) # Another way to reverse a list. Creates a new list

print(list(range(1,30))) # Create a range of items in a list

new_sentence = " ".join(["Hi", "my", "name", "is", "Kevin"])
print(new_sentence)

# List Unpacking
a,b,c, *other, d = [1,2,3, 4, 5, 6, 7, 8, 9]
print(a, b, c)
print(other)

# Dictionary = Unordered key-value pairs
# Unordered = stored in different parts of memory
dictionary = {
    "a": [1,2,3],
    "b": "Hello",
    "c": True
}

print(dictionary["b"]) # Get value of that key
print(dictionary)

my_list = [
    {
    "a": [1,2,3],
    "b": "Hello",
    "c": True
    },
    {
    "a": [4, 5, 6],
    "b": "Hello",
    "c": True
    }
]

print(my_list[0]["a"][2])
print(dictionary["a"][1])

user = {
    "basket": [1,2,3],
    "greet": "Hello"
}

# Dictionary Methods
print(user.get("greet"))  # Get  value of that key
print(user.get("age", 55))  # Sets a default value if the key does not exist

user2 = {
    "basket": [1,2,3],
    "greet": "Hello",
    "age": 20
}

print("basket" in user2) # find if a key exists in the dictionary
print("greet" in user2.keys()) # Check if a key exists
print(20 in user2.values()) # Check if a values exists
user2.clear() # clears the dictionary
print(user2)

user2 = {
    "basket": [1,2,3],
    "greet": "Hello",
    "age": 20
}

user3 = user2.copy() # copies a dictionary
print(user2)
print(user3)

print(user2.pop("age")) # removes a key and its value
print(user2)

print(user2.popitem()) # randomly removes a key/value
print(user2)

user2 = {
    "basket": [1,2,3],
    "greet": "Hello",
    "age": 20
}

user2.update({"age": 55})  # updates a key/value in a dictionary
print(user2)

# Tuples = Immutable lists. Usually faster than lists
# If you don't need your list to change, use a tuple
# A good use for a tuple is lat/long coordinates
my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)

x,y,z,*other = (5,6,7,8,9)
print(x, y, z)
print(other)

print(my_tuple.count(5)) # get number of times a value appears in the tuple
print(my_tuple.index(3)) # get an index of the mentioned value
print(len(my_tuple)) # get the length of a tuple

# Sets = Unordered collections of 'unique' objects
my_set = {1,2,3,4,5}
my_set.add(100)
my_set.add(2)
print(my_set) # note the 2 was not added because there was already a 2 in the set

# return a collection with unique items
my_list = [1,2,3,4,4,5,5]
print(set(my_list))
print(1 in my_set)  # check if an item is in a set
my_set.clear() # Clears all items from a set
print(my_set)

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9, 10}

"""
.difference()
.discard()
.difference_update()
.intersection()
.isdisjoint()
.issubset()
.issuperset()
.union()
"""

print(my_set.difference(your_set))  # {1, 2, 3}
my_set.discard(5) # delete an item in a set
print(my_set)
my_set.difference_update(your_set) # remove the differences from my_set
print(my_set)

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9, 10}
print(my_set.intersection(your_set))  # {4,5}

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9, 10}
print(my_set.isdisjoint(your_set)) # Is there something in common

print(my_set.union(your_set)) # Unites the sets together and removing any duplicate
# print(my_set | your_set) also works as well

my_set = {4,5}
your_set = {4,5,6,7,8,9, 10}
print(my_set.issubset(your_set))  # True {4,5} is inside of the other set
print(your_set.issuperset(my_set)) # True


































