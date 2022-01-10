# Conditional Logic
is_old = True
is_licensed = True

if is_old:
    print("You are old enough to drive")
elif is_licensed:
    print("You can drive now")
else:
    print("You are not of age")

if is_old and is_licensed:
    print("You are old enough to drive")
else:
    print("You are not of age")

# Truthy and Falsey values
"""
None, False, 0, 0.0, [], {}. (), "", set(), and others
"""

password = "123"
user_name = "johnny"
if password and user_name:
    print("You have a user name and a password")

# Ternary Operator
# condition_if_true if condition else condition_if_false

is_friend = True
can_message = "Message allowed" if is_friend else "Not allowed to message"
print(can_message)

# Short Circuiting
is_friend = True
is_user = True

# notices is_friend is True and sees the or, so it ignores (short circuits) the second
if is_friend or is_user:
    print("Best friends forever")

is_friend = False
is_user = True

# The same with using and. It sees False and does not need to evaluate the second part
if is_friend and is_user:
    print("Best friends forever")

# Logical Operator
print(4 > 5)
print(4 < 5)
print(4 == 5)
print(1 >= 2)
print(1 != 2)
print( 3 <= 3)
print(not(True)) # not gives the opposite

print(True == 1)
# print(True is 1) # checks if the location in memory is the same

# for loops
# iterable = something that is able to get looped over
# Iterated = one by one checks each item in the collection
for item in "Zero to Mastery":
    print(item)

for item in (1,2,3,4,5):
    print(item)

# nested for loops
for item in (1,2,3,4,5):
    for x in ["a", "b", "c"]:
        print(item, x)

user = {
    "name": "Golem",
    "age": 5006,
    "can_swim": False
}

for item in user:
    print(item) # prints keys of the user dictionary

for item in user.items():
    print(item) # prints keys and values of the user dictionary

for item in user.values():
    print(item) # prints values of the user dictionary

for item in user.keys():
    print(item) # prints keys of the user dictionary

for key,value in user.items():
    print(key, value)  # prints keys and values of the user dictionary

# Counter = counts the items in our list and adds them together
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
    counter = counter + item
print(counter)

# range() function = produces a sequence of integers. (start, stop, step)
for number in range(0, 50, 2):
    print(number)  # prints 0 to 49

for number in range(10, 0, -1):
    print(number)  # prints 10 to 1

# create 3 lists
for i in range(3):
    print(list(range(10)))

# enumerate() = allows you to get the index number of each item
for i,char in enumerate("Hello"):
    print(i, char)

for i,char in enumerate((1,2,3)):
    print(i, char)

for i,char in enumerate(list(range(50))):
    if char == 25:
        print(f"index of 25 is: {i}")


