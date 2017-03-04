
userHand =input("scissors,rock, paper:")
import random
computerHand = random.random()


if  computerHand<= (.33):
    computerHand = "rock"
elif computerHand<= .66:
    computer = "scissors"
else:
    computerHand= "paper"

def game (first,second):
    if (first== second):
        print("it is tie")
    elif first=="rock":
        if second=="scissors":
            print("you chose",first)
            print(" computer chose",second)
            print("you win")
        else:
            print("you chose",first)
            print(" computer chose",second)
            print("you lose")

    elif first=="paper":
        if second=="rock":
            print("you chose",first)
            print(" computer chose",second)
            print("you win")
        else:
            print("you chose",first)
            print(" computer chose",second)
            print("you lose")
    elif first=="scissors":
        if second=="paper":
            print("you chose",first)
            print(" computer chose",second)
            print("you win")
        else:
            print("you chose",first)
            print(" computer chose",second)
            print("you lose")

game (userHand,computerHand)
            

    
