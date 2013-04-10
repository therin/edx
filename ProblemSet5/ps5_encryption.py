# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    listing = string.ascii_uppercase + string.ascii_lowercase
    def encript(x, shift):
        result = ""
        if x.isalpha():
            y = ord(x) + shift
            new_x = chr(y)
            if (new_x > "Z" and x.isupper()) or (new_x > "z" and x.islower()):
                    new_x = chr(ord(new_x) - 26)
            result = new_x
        return result
    myDict = { x: encript(x,shift) for x in listing }
    return myDict
    '''
    #myDic = dict.fromkeys(listing, 0)
    #print encript("a", shift)
    #    if x == chr(65+i)
    #for k,v in myDic:
    #myDict = { x: func(x) for x in listing } 
    #str.isalpha()
    #print myDict
    #print string.ascii_uppercase
    #dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
    #dict['Age'] = 8; # update existing entry
    #dict['School'] = "DPS School"; # Add new entry
    #print {chr(65+i) : i for i in range(25)}
    #>>> print {k : v for k, v in someDict.iteritems()} == someDict.copy()
    #1
'''

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    mydict = coder
    result = ""
    new_letter = ""
    varub = False

    for letter in text:
        for k in mydict:
            if letter == k:
                new_letter = mydict[k]
                varub = True
        if varub == False:
            result = result + letter
        else: 
            result = result + new_letter
            varub = False
    return result


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    text1 = ""

    text1 = applyCoder(text, buildCoder(shift))
    return text1

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.
    isWord(wordList, word)
    applyShift(message, 26-k)
    text: string
    returns: 0 <= int < 26
    >>> 'Hello world!'.split('o')
    ['Hell', ' w', 'rld!']
    >>> '6.00x is pretty fun'.split(' ')
    ['6.00x', 'is', 'pretty', 'fun']
    """
    ### TODO
    counter = 0
    datab = {}
    result = 0

    for i in range(25,-1,-1):
        dec_text = applyShift(text, i)
        spl_text = dec_text.split(' ')
        for w in spl_text:
            if isWord(wordList, w):
                counter += 1
        datab[dec_text] = counter
        if counter >= max(datab.values()):
            result = i
        counter = 0
    #max_so_far = 0
    #for d in my_list:
    #    if d[1] > max_so_far:
    #        max_so_far = d[1]
    #print max_so_far


    return result

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    wordList = loadWords()
    text = getStoryString()
    shift = findBestShift(wordList, text)
    answer = applyShift(text, shift)
    return answer


#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    #applyShift(wordList, bestShift) == 'Not yet implemented.'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
