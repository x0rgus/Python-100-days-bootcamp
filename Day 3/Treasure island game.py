print('''\u001b[31;1m  _______                                  _     _                 _ 
 |__   __|                                (_)   | |               | |
    | |_ __ ___  __ _ ___ _   _ _ __ ___   _ ___| | __ _ _ __   __| |
    | | '__/ _ \/ _` / __| | | | '__/ _ \ | / __| |/ _` | '_ \ / _` |
    | | | |  __/ (_| \__ \ |_| | | |  __/ | \__ \ | (_| | | | | (_| |
    |_|_|  \___|\__,_|___/\__,_|_|  \___| |_|___/_|\__,_|_| |_|\__,_|



\u001b[0m''')
print("Welcome to treasure island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go? (LEFT/RIGHT)")
answer = input()
answer = answer.lower()

match answer:
    case "left":
        print("you come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or "
              "type 'swim' to swim across. ")
        answer = input()
        answer = answer.lower()
        match answer:
            case "wait":
                print("you get on the boat, you cross the lake and arrive at the island. ")
                print("there is 3 doors in front of you, a red one, a blue one and a yellow one.")
                print("type the color of the door you want to open.")
                answer = input()
                answer = answer.lower()

                match answer:
                    case "blue":
                        print("\u001b[31;1mIt's a room full of beasts, game over\u001b[0m")
                    case "red":
                        print("\u001b[31;1mits a room full of fire, game over\u001b[0m")
                    case "yellow":
                        print("You found the treasure.")
                        print("\u001b[36;1mYou win!\u001b[0m")
                    case _:
                        print("\u001b[31;1mGame over\u001b[0m")

            case _:
                print("\u001b[31;1mYou were attacked by a trout, game over\u001b[0m")

    case _:
        print("\u001b[31;1myou fell into a whole, game over\u001b[0m")
