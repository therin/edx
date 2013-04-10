from ps4a import *
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
  
    # Create a new variable to store the maximum score seen so far (initially 0)
    score = 0
    max_score = 0 

    # Create a new variable to store the best word seen so far (initially None)
    best_word = "" 

    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word
    # return the best word you found.
    if best_word == "":
        return "None"
    else:
        return best_word



# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total_score = 0
    # As long as there are still letters left in the hand:
    while compChooseWord(hand, wordList, n) != "None":
        # Display the hand
        print "Current hand: " ,
        str(displayHand(hand))
        print
        # Ask user for input
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        # End the game (break out of the loop)
        if word == ".":
            break
        # Otherwise (the input is not a single period):
        # If the word is not valid:
        # Reject invalid word (print a message followed by a blank line)
        else:
            if not isValidWord(word, hand, wordList):
                print "Invalid word, please try again."
            else:
        # Otherwise (the word is valid):
        # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
        # Update the hand
                total_score = total_score + getWordScore(word, n)
                print '"'+ word + '"' + " earned " + str(getWordScore(word, n)) + " points. Total: " + str(total_score) + " points."
                print
                hand = updateHand(hand, word) 
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if word == ".":
        print "Goodbye! Total score: " + str(total_score) + " points."
    else:
        print "Run out of letters. Total score: " + str(total_score) + " points."

wordList = loadWords()
hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
n = 9
print compPlayHand(hand, wordList, n)