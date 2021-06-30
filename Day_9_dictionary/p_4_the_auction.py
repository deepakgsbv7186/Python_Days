import os
from art import logo
begin = False
bid_details = {}
# auction logo
print(logo)
# a function which takes a dictionary {} as input parameter 
# and take care of max bid 
def choose_winner(bid_record):
    os.system("cls")
    max_bid = 0
    name = ""
    for bidder in bid_record:
        name = bidder
        if bid_record[bidder] > max_bid:
            max_bid = bid_record[bidder]
    print(f"Winner Bid:₹ {max_bid} by {bidder}")

# while loop with run again functionality
while not begin:
    print("Welocme to Secret Auction")
    bidder_name = input("What's Your Name: ")
    bid_value = int(input("Bid Value:₹ "))
    # add all inputs in the form of dictionary
    bid_details[bidder_name] = bid_value
    print("Is Anyone else want to bid?")
    choice = input("(Yes/No): ").lower()
    if choice == "yes":
        os.system("cls")
    else:
        begin = True
        choose_winner(bid_details)
        

