#nested conditionals

height = int(input("what is your height?"))
if height >= 120:
    print("you're tall enough for the ride")
    age = int(input("what is your age?"))
    if age < 12:
        print("Please pay 5$")
    elif age <= 18:
        print("please pay 7$")
    elif age > 18:
        print("please pay 12$")
else:
    print("you cant ride the rollercoaster")
