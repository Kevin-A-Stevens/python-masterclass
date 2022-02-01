from random import randint
import sys

# Run with python3 random_game.py 1 10
# generate a number 1 to 10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# get input from user


# check input is a number 1 to 10
while True:
    try:
        guess = int(input("Guess a number 1 to 10:  "))
        if 0 < guess < 11:
            if guess == answer:
                print("You are correct!")
                break
            break
        else:
            print("Please enter a number 1 through 10")
    except ValueError:
        print("Please enter a number")
        continue

# check if number is the right guess or ask again



