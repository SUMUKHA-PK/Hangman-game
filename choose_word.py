# This is the file that maintains the dictionary
# Words can be added or removed by inserting it into the array maintained as "word_set" below  (Only add words in caps)
# Everytime, a random word is returned to the game for the user to play

import random

def return_word():
    word_set = ["COMPUTER","FUZZY","SUMUKHA","CONSTANTINOPLE","VEYRON","EXORCIST","QUINTILLION","PLATEAU","SENNHEISER"]

    l = len(word_set)

    rand_num = random.randint(0,l-1)

    return word_set[rand_num]
