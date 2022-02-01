my_file = open("test.txt")

print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>

print(my_file.read())  # uses a curser to read files
my_file.seek(0) # moves curser to beginning
print(my_file.read())
my_file.seek(0) # moves curser to beginning
print(my_file.readline())  # reads one line the curser is on

my_file.close() # closes the file once you are done with it

# Do not need to close the file using with. Closes automatically
with open("test.txt") as my_file:
    print(my_file.readline())

# mode = read only
with open("test.txt", mode="r") as my_file:
    print(my_file.readline())

# mode = read and write
with open("test.txt", mode="r+") as my_file:
    text = my_file.write("Hey it is me!")
    print(text)  # 13

print(my_file)

# mode = append
with open("test.txt", mode="a") as my_file:
    text = my_file.write("I love Python")
    print(text)



# mode = w creates a new file if it doesn't exist
with open("me.txt", mode="w") as my_file:
    text = my_file.write("I love Python")
    print(text)

