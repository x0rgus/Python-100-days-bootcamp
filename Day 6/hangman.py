from hangman_assets import HANGMANPICS, words
import random
import time

# parameters
number_words = len(words)
word_index = random.randint(0, number_words-1)
word = words[word_index]

# creates a list of characters based on random word
word = [x for x in word]

MAX_WRONG = len(HANGMANPICS) -1
matches = 0


# creates empty letters display based on the lenght of the word
display = []
for letter in word:
    display.append("_")

list_pointer = 0
hangman_pointer = 0
victory = False
lives = 6

# initial screen
while matches < len(word) and lives > 0:
    print(HANGMANPICS[hangman_pointer], end="")
    print(display)
    userinput = input(f"\n Please type a letter (the solution is {word}")
    userinput = userinput.lower()
    time.sleep(1)
    if userinput in word:
        for position in range(len(word)):
            letter = word[position]
            if letter == userinput:
                display[position] = letter
                matches += 1
    else:
        lives -= 1
        hangman_pointer += 1
    print(display)
if lives == 0:
    print(HANGMANPICS[hangman_pointer])
    print("you lose!")
else:
    print("You win!")
# replaces empty letter in display with correct letter

