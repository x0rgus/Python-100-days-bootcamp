from hangman_assets import HANGMANPICS, words
import random

# parameters
number_words = len(words)
word_index = random.randint(0, number_words-1)
word = words[word_index]
word = [x for x in word]
MAX_WRONG = len(HANGMANPICS) -1
blankletters = len(word)

print(HANGMANPICS[0], end="")
for space in word:
    print("_ ", end="")
