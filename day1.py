from art import *

Art=text2art("coffee")
print(Art)


print("-----------------------------")
print("-----------------------------")


def highestBidder(bidders):
    max = 0
    highest = {}
    
    for i, j in bidders.items():
        if j>=max:
            max = j
            
    for i, j in bidders.items():
        if j==max:
            print(f"{i} is the highest bidder")
            

bidders = {
    
}
moreBidders = "Yes"


while moreBidders == "Yes":
    name = input("Your name :")
    bid = int(input("Enter the bid amound : "))
    bidders[name] = bid
    
    moreBidders = input("are there any more bidders : ")

highestBidder(bidders)