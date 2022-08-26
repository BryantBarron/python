import os

def clear_screen():
    os.system('clear')

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for key in bidding_record:
        bid = bidding_record[key] 
        if bid > highest_bid:
            highest_bid = bid
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    cont = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if cont == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif cont == "yes":
        clear_screen()




