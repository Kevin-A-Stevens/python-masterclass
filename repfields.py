age = 24

# str function coerce an integer into a string
print("My age is " + str(age) + " years")

# Format strings is a better way
print("My age is {0} years".format(age))

print("There are {0} days in {1} and {2} days in {3}".format(31, "January", 28, "February"))

# formatting strings

for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

print("With formatting")

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))  # default 6 digits after decimal point
print("Pi is approximately {0:12.50f}".format(22 / 7))  # 50 digits after decimal point
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7)) # left align
