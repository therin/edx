# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    counter = 0
    for letter in secretWord:
         if letter in lettersGuessed:
                counter += 1
    if counter == len(secretWord):
        return True
    else:
        return False
   

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    my_list = []
    for letter in secretWord:
         if letter in lettersGuessed:
            my_list.append(letter)
         else:
            my_list.append("_ ")
    return "".join(my_list)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed. a = a.replace('l','')
    '''
    # FILL IN YOUR CODE HERE...
    all_list = string.ascii_lowercase
    for letter in lettersGuessed:
        if letter in all_list:
           all_list = all_list.replace(letter,"")
    return all_list

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    lettersGuessed = [] # The letters that have been guessed so far.
    mistakesMade = 0
    attempts = 8    #The number of incorrect guesses made so far.
    availableLetters = [] #The letters that may still be guessed. 
    #Every time a player guesses a letter, the guessed letter must be removed from availableLetters 
    #(and if they guess a letter that is not in availableLetters, you should print a message telling 
    #them they've already guessed that - so try again!).

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print "-------------"
    while isWordGuessed(secretWord, lettersGuessed) is False:
        print "You have " + str(attempts) + " guesses left."
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ')
        guessInLowerCase = guess.lower()
        availableLetters = getAvailableLetters(lettersGuessed)
        if guessInLowerCase in secretWord and guessInLowerCase not in lettersGuessed:
            lettersGuessed.append(guessInLowerCase)
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
        elif attempts <= 1:
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            print "-------------"
            print "Sorry, you ran out of guesses. The word was " + secretWord + "."
            break
        elif guessInLowerCase in lettersGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(guessInLowerCase)
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            attempts -= 1
        print "-------------"
        if isWordGuessed(secretWord, lettersGuessed) is True:
            print "Congratulations, you won!"
            break
                  


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
#secretWord = chooseWord(wordlist).lower()
hangman("y")
