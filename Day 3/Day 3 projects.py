# all minor projects from day 3 with a CLI

print("\033[1;32m Please choose an option below:\n")
print("\033[1;32m 1. BMI calculator")
print("\033[1;32m 2. Leap year checker")
print("\033[1;32m 3. Love calculator")
print("\033[1;32m 4. Rollercoaster")
print("\033[1;32m 5. Pizza order")
choice = input()
print("\u001b[0m")

if choice == "1":
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    bmi = int(weight) / (float(height) ** 2)
    bmi = round(bmi)
    str(bmi)
    print(bmi)
    group = ""
    if bmi <= 18.5:
        group = "underweight"
    elif bmi <= 25:
        group = "normal weight"
    elif bmi <= 30:
        group = "slightly overweight"
    elif bmi <= 35:
        group = "obese"
    else:
        group = "clinically obese"

    print(f"Your BMI is {bmi}, you are {group}")

if choice == "2":
    def leapcheck(year):
        if year % 4 == 0:
            result = "Leap year."
        elif year % 100 == 0:
            result = "Leap year."
        elif year % 400 == 0:
            result = "Leap year."
        else:
            result = "Not leap year."
        return result


    year = int(input("which year do you want to check?"))
    year = leapcheck(year)

    print(year)

if choice == "3":
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")

    name1 = name1.lower()
    name2 = name2.lower()
    names = str(name1) + str(name2)
    count1 = names.count("t") + names.count("r") + names.count("u") + names.count("e")

    count2 = names.count("l") + names.count("o") + names.count("v") + names.count("e")

    finalcount = str(count1) + str(count2)

    finalcount = int(finalcount)
    if finalcount < 10 or finalcount > 90:
        print(f"Your score is {finalcount}, you go together like coke and mentos.")
    elif 40 < finalcount < 50:
        print(f"Your score is {finalcount}, you are alright together.")
    else:
        print(f"Your score is {finalcount}.")

if choice == "4":
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

if choice == "5":
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

else:
    print("invalid choice")