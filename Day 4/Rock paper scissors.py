import random

# visuals
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
##

userchoice = int(input("Choose one: 1-rock 2-paper 3-scissors"))
computerchoice = random.randint(1,3)
wins = bool(0)
draw = bool(0)

print("you choose \n")
match userchoice:
    case 1:
        print(rock)
    case 2:
        print(paper)
    case 3:
        print(scissors)

print("the computer choses \n")
match computerchoice:
    case 1:
        print(rock)
    case 2:
        print(paper)
    case 3:
        print(scissors)

if userchoice == 1 and computerchoice == 1:
    wins =0
    draw =1
elif userchoice == 1 and computerchoice == 2:
    wins =0
    draw =0
elif userchoice == 1 and computerchoice == 3:
    wins =1
    draw =0
elif userchoice == 2 and computerchoice == 1:
    wins =1
    draw =0
elif userchoice == 3 and computerchoice == 1:
    wins =0
    draw =0
elif userchoice == 2 and computerchoice == 2:
    wins =0
    draw =1
elif userchoice == 3 and computerchoice == 3:
    wins =0
    draw =1

if wins == 0 and draw == 0:
    print("you lose!")
elif wins == 1 and draw == 0:
    print("you win!")
elif wins == 0 and draw == 1:
    print("Draw!")