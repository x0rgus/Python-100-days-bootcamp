from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

run = True
menu1 = Menu()
coffemaker1 = CoffeeMaker()
moneymachine1 = MoneyMachine()

while run:
    input = input(print(
        "Please choose a drink or type 'report' for a report of resources:\n 1.Espresso \n 2.Latte \n 3.Cappuccino\n type 'quit' to exit")).lower()
    match input:
        case "report":
            coffemaker1.report()
        case "espresso" | "latte" | "cappuccino":
            choice = menu1.find_drink(input)
            if coffemaker1.is_resource_sufficient(choice) == True:
                if moneymachine1.make_payment(choice.cost) == True:
                    coffemaker1.make_coffee(choice)
            else:
                print("Not enough resources")
            print(choice.name)
        case "quit":
            run = False
        case _:
            print("invalid choice")
