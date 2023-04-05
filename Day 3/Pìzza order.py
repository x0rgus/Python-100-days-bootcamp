# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = int(0)

if size == "S" or size == "s":
    bill += 15
if size == "M" or size == "M":
    bill += 20
if size == "L" or size == "L":
    bill += 25

if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")
