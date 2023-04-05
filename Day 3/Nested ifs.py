# nested conditionals

height = int(input("what is your height in centimeters?"))
bill = 0
if height >= 120:
    print("you're tall enough for the ride")

    age = int(input("what is your age?"))
    if age < 12:
        bill = bill + 5
        print("Your ticket will be 5$")
    elif age <= 18:
        bill = bill + 7
        print("Your ticket will be 7$")
    elif age > 18:
        bill = bill + 12
        print("Your ticket will be 12$")

    wants_photo = str(input("Do you want photos of the ride? price: 3$ (Y/N)"))

    if wants_photo == "Y" or wants_photo == "y":
        bill += 3

    print(f"Total price:{bill}")
else:
    print("you cant ride the rollercoaster")
