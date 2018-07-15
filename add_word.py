# This script can be used to add words to the set of existing words in the script choose_word
# Enter the word to be added and the exact file location to add the word into the existing set of words
# A backup of the existing file is made as a '.bak' file in the location of the file

import os
import sys
import fileinput as  fi

new_word = input("Enter the new word to be added: ")

file_location = input("Enter the file location: ")

file_ptr = open(file_location,'r+')

with fi.FileInput(file_location,inplace=True,backup='.bak') as file:
    for line in file:
        print(line.replace("\"]","\",\""+new_word+"\"]"),end='')
