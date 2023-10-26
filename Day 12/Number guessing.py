import random

random_number = 0
max_attempts = 0
turn_counter = 0
difficulty = 0
player_number = 0
game_state = 0


def greet():
    global difficulty
    global max_attempts
    difficulty = 0
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 0 and 100")
    dif = input(print("Choose a difficulty, type 'easy' or 'hard': "))
    match dif:
        case "easy":
            difficulty = 0
            max_attempts = 10
        case "hard":
            difficulty = 1
            max_attempts = 5
        case _:
            print("Invalid choice! exiting")
            exit()


def main():
    global random_number
    global player_number
    global game_state
    global max_attempts
    global turn_counter
    random_number = random.randint(0, 100)
    player_number = 0
    game_state = 0
    turn_counter = 0

    while game_state == 0 and turn_counter < max_attempts:
        remaining_attempts = max_attempts - turn_counter
        print(f"you have {remaining_attempts} remaining attempts")
        player_number = int(input(print("Guess a number!")))
        if random_number > player_number:
            print("You've guessed too low! try again")
            turn_counter += 1
        elif random_number < player_number:
            print("You've guessed too high! try again")
            turn_counter += 1
        elif random_number == player_number:
            print("You've guessed correctly!")
            game_state = 1

    if game_state == 1:
        print("You've won!")
    if turn_counter == max_attempts:
        print("You've run out of attempts! game over")
        game_state = 2
        exit()


greet()
main()