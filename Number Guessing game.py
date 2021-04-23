#Number Guessing game
import random
import time
from tqdm.auto import tqdm

#loading bar animation
def animate():
    for x in tqdm(range(100)):
        print(" ", end='\r')

def hint(n):
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

def checkAns(n,ans):
    global result
    if ans==n:
        print("You found the correct answer!")
        result = True
    else:
        print("Ooopsies, wrong answer please try again")
        result = False
    return result

def initProfile():
    global n, name, score
    n = random.randint(0,1000)
    name = " "
    score = 0

    print("Hello welcome to Number Guessing Game by ikhmalloy...")
    name = input("Please enter your name here: ")

    print(f"\nHi {name} For startup I will set your score to 10. You guess it right I add more points") #use 'f' as apa tah lupo den haa
    print("But if you guess it wrong, points will be deducted")
    score = 10
    time.sleep(3)

def ifWrong(result, score):
    while result == False:
      ans = input("\nEnter you guess here: ")
      ans = int(ans)
      checkAns(n,ans)  

def scoring(result):
    if result == True:
        score += 10
    else:
        score -= 10
    return score

#main
animate()
initProfile()
time.sleep(3) 
print("\nA random number was generated just now!")
print("Can you guess the number?")
hint(n)
ans = input("\nEnter you guess here: ")
ans = int(ans)
checkAns(n,ans)
ifWrong(result)