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
elif finalcount > 40 and  finalcount < 50:
    print(f"Your score is {finalcount}, you are alright together.")
else:
    print(f"Your score is {finalcount}.")
