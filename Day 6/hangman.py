from hangman_assets import HANGMANPICS, words
import random

# parameters
number_words = len(words)
word_index = random.randint(0, number_words-1)
word = words[word_index]
word = [x for x in word]
MAX_WRONG = len(HANGMANPICS) -1
blankletters = len(word)
display = []

print(HANGMANPICS[0], end="")
for letter in word:
    display.append("_")
print(display)
userinput = input("\n Please type a letter")
userinput = userinput.lower()

for letter in word:
    if userinput == letter:
        print("correct letter")
    elif not userinput == letter:
        print("incorrect letter")
