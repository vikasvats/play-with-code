# I will work on this project later

import random
from words import words

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

def hangman():
    word = get_valid_word(words)
    word_letter = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_latters = set() #what the user has guessed

    # getting user input
    used_latter = input('guess a latter: ').upper()
    if user_letter in alphabet - used_latters:
        used_latters.add(user_letter)
