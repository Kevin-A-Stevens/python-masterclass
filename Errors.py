# Error Handling
## TypeError - incompatible data types (1 + "Hello")
## SyntaxError - print(Hello")
## NameError - 1 + name (name is not defined)
## IndexError - li = [1,2,3]; print li[5]
## keyError - di = {"a": 1}; di["b"]
## ZeroDivisionError - print(5/0)

while True:
    try:
        age = int(input("What is your age? ")) # If user enters a, will get a ValueError
        print(age)
    except:
        print("Please enter a number")
    else:
        print("Thank you")
        break

while True:
    try:
        age = int(input("What is your age? ")) # If user enters a, will get a ValueError
        10/age
        #raise ValueError("Hey, something went wrong")
    except ValueError:
        print("Please enter a number")
        continue
    except ZeroDivisionError:
        print("Please enter an age higher than 0")
        continue
    else:
        print("Thank you")
        break
    finally:
        print("Ok, I am finally done")

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Please enter numbers. {err}")

print(sum("1", 2))

