from Assets import *

debug = True


def insert_mode(drink_price):
    value = 0
    while value <= drink_price:
        print(f"Money inserted: ${value}")
        coin = input("Please insert coins \n 1-Penny(1 cent) \n 2-Nickel(5 cents) \n 3-Dime(10 cents) \n 4-Quarter(25 cents)")
        match coin:
            case "1":
                value = (value + 0.01)
            case "2":
                value = (value + 0.05)
            case "3":
                value = (value + 0.10)
            case "4":
                value = (value + 0.25)
            case _:
                print("invalid choice")
    change = (value - drink_price)
    change = round(change, 2)
    print(f"Done! here is your change:${change} \n enjoy your drink")
def check_res():
    a = resources
    wvalue = a["water"]
    mvalue = a["milk"]
    cvalue = a["coffee"]
    return wvalue, mvalue, cvalue


def format_input(inp):
    text = ""
    match inp:
        case "1":
            text = "espresso"
        case "2":
            text = "cappuccino"
        case "3":
            text = "latte"
        case _:
            print("Invalid argument passed to format input function!")
            exit
    return text


def get_item_money_cost(item):
    values = MENU[item]
    print(item)
    try:
        money_cost = values["cost"]
    except KeyError:
        pass
    return money_cost


def get_item_res_cost(item):
    values = MENU[item]

    print(item)
    try:
        wvalue = values["ingredients"]["water"]
    except KeyError:
        wvalue = 0

    try:
        mvalue = values["ingredients"]["milk"]
    except KeyError:
        mvalue = 0

    try:
        cvalue = values["ingredients"]["coffee"]
    except KeyError:
        cvalue = 0
    return wvalue, mvalue, cvalue


def interface():
    answer = input(print("Welcome! what would you like to order?\n1-Espresso \n2-Cappuccino \n3-Latte")).lower()
    match answer:
        case "1" | "2" | "3":
            answer = format_input(answer)
            rescost = get_item_res_cost(answer)
            moncost = get_item_money_cost(answer)
            print(rescost)
            print(moncost)
            insert_mode(moncost)

        case "report":
            current_w, current_m, current_c = check_res()
            print(f"Water:{current_w}, Milk:{current_m}, Coffee:{current_c}")
        case _:
            print("invalid choice")


if debug:
    # print(get_item_res_cost(MENU["latte"]))
    print(check_res())
    interface()
