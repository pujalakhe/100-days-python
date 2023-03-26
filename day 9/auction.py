from pickle import TRUE
import os


print("*******WELCOME TO TODAY'S ACUTION**********")
bids={}
bidding_finished=False
def highest_bidder(bidding_record):    #bidding_recod={"puza":"250","puzan":"150"}
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"the winner is {winner} with bidding amt of Rs.{highest_bid}")
    
while not bidding_finished:
    name=input("enter yor name:\n")
    price=int(input("enter yor bid price\nRs."))
    bids[name]=price   #key is name and value is price 
    should_continue=input("Are there other bidders?\nType 'yes' or 'no':")
    if should_continue=="no":
        bidding_finished=TRUE
        highest_bidder(bids)
    elif should_continue=="yes":
        os.system('cls')#to clear the screen

    