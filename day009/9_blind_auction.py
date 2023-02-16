def winner(bidders):
    tmp = 0
    win = ""
    for key in bidders:
        if bidders[key] > tmp:
            tmp = bidders[key]
            win = key
    print(f"The winner is {win} with a bid of ${tmp}")


bidders = {}
choice = False
while not choice:
    name = input("What`s your name?: ")
    bid = int(input("What`s your bid?: $"))
    bidders[name] = bid
    restart = input("Are where any other bidders? Type 'yes' or 'no' ")

    if restart == "no":
        winner(bidders)
        choice = True

