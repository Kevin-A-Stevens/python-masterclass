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
