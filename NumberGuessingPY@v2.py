'''
so kita nak ada flow ni:

-Profile
    -> Setup nama
    -> setup initital score

-Generate random number animation
    ->pakai tqdm
    ->import random

-Calculate score
    ->check kalau jawapan betul or not
    ->update score tambah 5 kalau salah vice versa

-concl
    -tunjuk final score

-stop game or continue play
'''

import random
from tqdm.auto import tqdm
import time

name = ""
score = 0
n = 0

def profile():
    global name,score
    print("Welcome to Guess The Number Game!")
    name = input("Enter your name here: ")
    print(f"Your starting score will be at {score}\n\n")

def initNum(score):
    print("\nThe game will start now...")
    global n
    n = random.randint(1,100)
    for x in tqdm(range(100)):
        print(" ", end='\r')
    time.sleep(5)
    print(f"\nA random number was generate. Guess what it is, {name}!")
    print(f"Current score: {score}")

def calScore(n):
    global score
    print("\nThese are your hints:")
    if n>0 and n<=250:
        print(" The number is less than 250")
    elif n>250 and n<=500:
        print(" The number is greater than 250 but less than 500")
    elif n>=500:
        print(" Fuh you got the hard one ey? The number is greater than 500 but less than 1000!")
    
    txt = " The number is {} from the number"
    print(txt.format(n-40))
    print(" Add it by 40")

    ans = input("Enter your guess here:")
    ans = int(ans)

    #check correct ans or not
    if ans == n:
        print("Congrats you got it correct!")
        score+=10
    elif ans != n:
        print("Ooops, wrong answer")
        score -=10

def finalScore(score,name):
    print("\nCongrats on completing the game! Here's a summary:\n")
    print(f"Name : {name}\n")
    print(f"Score : {score}\n")


#function call
profile()
again = True
while again: 
    initNum(score)
    calScore(n)
    repeat=input("\nDo you want to play again?: ")
    if repeat =="Yes" or repeat == "yes":
        again = True
    else:
        again=False
finalScore(score,name)