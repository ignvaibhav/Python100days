from art import *
import random
import os
import platform

def clrscr():
    # Check the operating system
    if platform.system() == "Windows":
        os.system("cls")  # Clear screen command for Windows
    else:
        os.system("clear")  # Clear screen command for MacOS/Linux


def blackJack():
    clrscr()
    
    print(text2art("bLACKjACK"))
    print("-----------------------------")
    print("-----------------------------\n\n")
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    userSet = [random.choice(deck), random.choice(deck)]
    computerSet = [random.choice(deck), random.choice(deck)]
    print(f"Your cards : {userSet}\t score : {userSet[0]+userSet[1]}")
    print(f"Computer : {computerSet[0]}")
    
    pickOrStand = input("Pick or Stand? P or S : ")
    
    if pickOrStand == "P":
        pick(deck, userSet, computerSet)
        
    elif pickOrStand == "S":
        # print(type(deck))
        stand(deck, userSet, computerSet)

def stand(deck, userSet, computerSet):
    # print(type(deck))
    userTotal = sum(userSet)
    computerSet.append(random.choice(deck))
    computerTotal = sum(computerSet)
    print("\n")
    print("\n")
    
    print(f"Your_cards : {userSet}\t your score : {userTotal}")

    print(f"Computer's cards : {computerSet}\t Computer score : {computerTotal}")
    

    if computerTotal >= 22:
        print("You won!")
    elif userTotal >= 22:
        print("You lose")
    elif computerTotal > userTotal:
        print("You lose")
    elif computerTotal == userTotal:
        print("Draw")
    else:
        print("You lose")
        
    reply = input("You want to play again? Y or N : ")
    if reply == "Y":
        blackJack()
    else:
        print("Thanks for playing!")
        

    
def pick(deck, userSet, computerSet):
    userSet.append(random.choice(deck))
    userTotal = sum(userSet)
    computerTotal = sum(computerSet)
    
    if 22>computerTotal<userTotal:
        computerSet.append(random.choice(deck))
        computerTotal = sum(computerSet)

    
    print(f"Your cards : {userSet}\t your score : {userTotal}")
    print(f"Computer's cards : {computerSet}\t Computer score : {computerTotal}")
    

    if computerTotal >= 22:
        print("You won!")
    elif userTotal >= 22:
        print("You lose")
    elif computerTotal > userTotal:
        print("You lose")
    elif computerTotal == userTotal:
        print("Draw")
    else:
        print("You lose")
        
    reply = input("You want to play again? Y or N : ")
    if reply == "Y":
        blackJack()
    else:
        print("Thanks for playing!")





            
        
        
blackJack()