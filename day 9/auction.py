bids = {}

bidding_finished = False


def find_highest_bid(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("what is your name?")
    price = int(input("what is your bid?"))
    bids[name] = price
    print("\n\n\n\n\n\n\n")
    run = input("Are there any other bidders? Type 'yes' or 'no'")
    if run == "no":
        bidding_finished = True
        find_highest_bid(bids)
