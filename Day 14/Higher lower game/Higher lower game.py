from art import *
from game_data import data
import random


def generate_person():
    person = random.choice(data)
    return person


def high_low(count1, count2):
    if count1 >= count2:
        return True
    elif count2 > count1:
        return False


points = 0
state = 0
print(logo)
person1 = generate_person()
person2 = generate_person()
while state == 0:
    match state:
        case 0:
            if points > 0:
                person1 = person2
                person2 = generate_person()
            # print(person1, person2)
            # use to debug
            print(f"You have {points} Points!")
            print("Does {name} ({description}) ({follower_count} Followers) has more followers than ".format(**person1),
                  end="")
            print("{name} ({description})?".format(**person2))
            r = str(input("")).lower()
            match r:
                case "y":
                    guess = high_low(person1["follower_count"], person2["follower_count"])
                    if guess == True:
                        points += 1
                    else:
                        state = 1
                case "n":
                    guess = high_low(person2["follower_count"], person1["follower_count"])
                    if guess == True:
                        points += 1
                    else:
                        state = 1

print("Game over!")
