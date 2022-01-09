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















