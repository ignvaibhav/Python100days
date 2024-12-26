# connect the coffeeMachineData.py file before running this


from art import *
from coffeeMachineData import *
import os

import platform

def clrscr():
    # Check the operating system
    if platform.system() == "Windows":
        os.system("cls")  # Clear screen command for Windows
    else:
        os.system("clear")  # Clear screen command for MacOS/Linux

clrscr()
print(text2art("Coffee Machine"))

print("-----------------------------")
print("-----------------------------\n\n")


def welcome():
    welcomeInput = input("\nType to operate (report/start): ")
    if welcomeInput == "report":
        resourceLeft(resource)
    elif welcomeInput == "start":
        start(coin, price, resource)
    else:
        print("Invalid Input!")
        welcome()

def resourceLeft(resource):
    print("\n------------------------------")
    print("------------------------------\n")
    print(f"current resource status :\n")

    for i, (key, value) in enumerate(resource.items()):
        print(f"{key} : {value}")
        
    print("\n")
    welcome()

def resourceChecker(coffeeName):
    coffeeResources = coffeeRequirements.get(coffeeName)
    # print(type(coffeeResources))
    
    if not coffeeResources:
        print(f"'{coffeeName}' is not available.")
        welcome()
        return
    
    for i, j in coffeeResources.items():
        if resource[i] < j:
            print(f"Not enough {ingredient} for {coffeeName}.")
            return False
    return True
    

def payment(coffeeName):
    print(f"You have to pay ${price[coffeeName]}\n")
    quaterPayment = int(input("Enter the number of Quaters : "))
    dimPayment = int(input("Enter the number of Dime : "))
    nickelPayment = int(input("Enter the number of Nickle : "))
    penniePayment = int(input("Enter the number of Pennie : "))

    totalPaid = round(sum([quaterPayment*0.25,dimPayment*0.10,nickelPayment*0.05,penniePayment*0.01]),2)
    print("Payment Successful")
    print(f"\ntotal amount paid ${totalPaid}\n")
    
    if totalPaid < price[coffeeName]:
        print(f"You have to pay {price[coffeeName]-totalPaid} more\n")
        
        quaterPayment = int(input("Enter the number of Quaters : "))
        dimPayment = int(input("Enter the number of Dime : "))
        nickelPayment = int(input("Enter the number of Nickle : "))
        penniePayment = int(input("Enter the number of Pennie : "))

        totalPaid += round(sum([quaterPayment*0.25,dimPayment*0.10,nickelPayment*0.05,penniePayment*0.01]),2)
        
        if totalPaid < price[coffeeName]:
            print("chala ja bsdk!")
            return
    
    elif totalPaid > price[coffeeName]:
        change = round(totalPaid - price[coffeeName], 2)
        print(f"Here's your change ${change}")
        makingCoffee(coffeeName)
    
    elif totalPaid == price[coffeeName]:
        print(f"thanks for the payment!")
        makingCoffee(coffeeName)


def makingCoffee(coffeeName):
    coffeeResource = coffeeRequirements.get(coffeeName)
    for i, j in coffeeResource.items():
        resource[i] -= j

    order(coffeeName)
    
    
def order(coffeeName):
    print(f"Thanks for your order, here's your {coffeeName}")
    welcome()
    
    
def start(coin, price, resource):
    print("\n---- Menu ----\n")
    for i in coffeeRequirements.items():
        print(f"{i[0]}")
    print("\n")
    coffeeName = input("What would you like to have? (espresso/latte/cappuccino) : ")
    resourceChecker(coffeeName)
    payment(coffeeName)
    

    
    

print("Coins we accept :\n")
for i, j in coin.items():
    print(f"{i} = {j}")
print("\n")

print("Welcome to the Coffee Machine simulator!")
welcome()
# payment(espresso)
