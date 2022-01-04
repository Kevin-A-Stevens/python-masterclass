print("Today ios a good day to learn Python")
print("Python is fun")
print("Python's strings and easy to use")
print("We can even use 'quotes' in strings")

# string concatenation
print("Hello" + " world")

# setting variables
greeting = "Hello"

# getting input from user
name = input("Please enter your name ")

print(greeting + " " + name)

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print()
print(parrot[-1])   # e = last character

# Slicing = start stop step. Note the : otherwise it's an index
print(parrot[0:6])  # Norweg
print(parrot[3:5])  # we
print(parrot[:9])   # Norwegian
print(parrot[10:])  # Blue

# Can also use negative numbers
print(parrot[-4:-2])    # Bl

# The step value
print(parrot[0:6:2])    #Nre

number = "9,223,372,354,875,607"
print(number[1::4])

# Slicing backwards
letters = "abcdefghijklmnopqrstuvwxyz"

# [::-1] is a Python Idiom
backwards = letters[::-1]
print(backwards)






