from art import *

Art=text2art("calculator")
print(Art)

print("-----------------------------")
print("-----------------------------\n\n")


def calculator():
    num1 = int(input("Enter the first number : "))
    print(f"+\n-\n*\n/")
    operation = input("Pick an operator : ")
    num2 = int(input("What's the next number : "))
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid operator!")
        return

    print(f"{num1} {operation} {num2} = {int(result)}")
    
    keepGoing = input("Do you want to continue or start a new one? Continue or New: ")
    
    if keepGoing == "Continue":
        while keepGoing == "Continue":
            
            print(f"+\n-\n*\n/")
            operation = input("Pick an operator : ")
            num2 = int(input("What's the next number : "))
            
            finalResult = 0
            if operation == "+":
                finalResult = result + num2
            elif operation == "-":
                finalResult = result - num2
            elif operation == "*":
                finalResult = result * num2
            elif operation == "/":
                finalResult = result / num2
            else:
                print("Invalid operator!")
                return
            
            print(f"{result} {operation} {num2} = {int(finalResult)}")
            result = finalResult
            keepGoing = input("Do you want to continue or start a new one? Continue or New : ")
    if keepGoing == "New":
        calculator()

    
calculator()