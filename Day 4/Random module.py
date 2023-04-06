# Random number and index demo
import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

npeople = (len(names))
random_choice = random.randint(0, npeople - 1)
payer = names[random_choice]
print(f"{payer} is going to buy the meal today!")
