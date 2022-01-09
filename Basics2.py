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



