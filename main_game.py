# Following is a computer simulation of the hangman game

import choose_word
import win

print("Welcome to Hangman!")

word = choose_word.return_word();
word_length = len(word)
number_of_chances = 8                                                           # Standard number of chances in a game of hangman
string = "-" * word_length

while(number_of_chances>0):
    print("The word now looks like this: "+string)
    print("You have %d guesses left." % number_of_chances)
    user_input = input("Your guess: ")
    user_input = user_input.upper()
    if(len(user_input)>1):
        print("Input only one character please!")
    elif((user_input==" ")|(user_input=="")):                                   # Check for  valid input
        print("Enter valid input!")
    else:
        flag=0
        for i in range(0,word_length):
            if((string[i]=="-")&(word[i]==user_input)):
                flag=1
                print("That guess is correct.")
                x = list(string)
                x[i]=user_input
                string="".join(x)
        if(flag==0):
            print("There are no "+user_input+"\'s in the word")
            number_of_chances-=1
    if(win.check_complete(string,word)==1):
        print("You guessed the word: "+word)
        print("You win!")
        break
    elif(number_of_chances==0):
        flag=0
        for i in range(0,word_length):
            if(string[i]=="-"):
                print("You\'re completely hung.")
                print("The word was: "+word)
                print("You lose.")
                break
