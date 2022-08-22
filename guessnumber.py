from pickle import TRUE
import random

print("HI! Do you want to play game with me?")

x = random.randint(1, 1001)

while True:
    userGuess = int(input("Enter number: "))
    
    if x > userGuess:
        print("You number is smaller.")

    if x < userGuess:
        print("You number is bigger.")

    if userGuess == x:
        print("You won!")
        break
    