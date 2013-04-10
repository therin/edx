import string
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

lettersGuessed = ['e','i','k','p','r','s']
print getAvailableLetters(lettersGuessed)

