from hangman_assets import HANGMANPICS, words
import random

# Generate random word
number_words = len(words)
word_index = random.randint(0, number_words-1)
word = words[word_index]

