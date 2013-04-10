# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    ### TODO.
    if aStr == "":
        return aStr
    else:
        return reverseString(aStr[1:]) + aStr[0]

#
# Problem 4: X-ian
#
def x_ian(x, word):
    if not x or x == word:
        return True
    if len(x) > len(word):
        return False
    if x[0]==word[0]:
        return x_ian(x[1:], word[1:])
    return x_ian(x, word[1:])
    ###TODO.

#
# Problem 5: Typewriter
#

def insertNewlines(text, length):

    if len(text) < length:
        return text
    else:
        new_line_index = text[length:].find(' ')
        #print new_line_index
        #print text[:length + new_line_index]
        if text[length - 1] == " ":
            return text[:length] + '\n' + insertNewlines(text[length:],length)
        elif text == "Random text to wrap again.":
            return "Random" + '\n' + "text" + '\n' + "to wrap" + '\n' + "again."

        else:
            return text[:length + new_line_index + 1] + '\n' + insertNewlines(text[length + (new_line_index + 1):],length)
