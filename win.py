# This module checks whether the user has won the game of hangman

def check_complete(string,word):
    l = len(word)
    count = 0
    for i in range(0,l):
        if(string[i]==word[i]):
            count+=1
    if(count==l):
        return 1
    else:
        return 0
