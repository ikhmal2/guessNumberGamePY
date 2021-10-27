import random

print("Hello and welcome to a number guessing game!\n")
topNumber = input("Please enter a number: ")

if topNumber.isdigit:
    topNumber = int(topNumber)
elif topNumber <= 0:
    print("Please enter number greater than 0!")
    exit()
else:
    print("Please enter a number!")
    exit()

randomNumber = random.randint(0,topNumber)
counter = 0

while True:
    counter += 1
    guess = input("Guess the number: ")
    guess = int(guess)

    if guess == randomNumber:
        print("You got it correct!")
        break
    
    elif guess < randomNumber:
        print("You are below the number!")
        continue
    
    elif guess > randomNumber:
        print("You are above the number!")
        continue
    
    else:
        print("Please enter a number!")
        continue

print("You have tried",counter,"times!")