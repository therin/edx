import string
from ps5_encryption import *
from ps5_recursion import *


'''
I think the find function, which returns the first index of a substring, and -1 if the substring is not in the 
string, can be useful for this problem. Example: 'abc'.find('c') returns 2, and 'lizard'.find('w') 
returns -1.

I check if text at position [lineLength - 1] is space or a character...
no need for helper, wrapper functions, i only used the find() built in string function
hope this helps and it's ok with forum rules...

Something like text[lineLength:] will give you the line length you need. Keep doing it until 
you run out of text. You'll have to find the spaces though.

base case, when text length smaller or equal to lineLength:
     return text
otherwise:
     determine where to insert newline,
     return lineText + newlinecharacter + 
                  insertNewLines(restOfText, lineLength)
I used string.find(' ') on the text that comes after lineLength, then used that information to determine 
where to split for the recursive call. You have to be meticulous; I needed to use print statements to debug 
until I got it right.
For ex. a helper function could look like this:
def insertNewlinesRec(words, position, maxLineLength): ...
where it is called as:
insertNewlinesRec(words, 0, lineLength)
 (it could be done in 3 row if do not store result of text.find() in a variable)
'''

#def insertNewlinesRec(text, position, length):
 #   return (text[:length]+'\n'+ insertNewlines(text[length:],length))


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

print insertNewlines('Random text to wrap again.', 5)
print
print insertNewlines('While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.', 15)
print
print insertNewlines('nxrs puv rcdfhqkz svub nocfvhke xphml yndoxk dnlpxoj kqsme xei fmnq tacnmgrw wxy crhbmv dbt agzksru qledpnju stb', 24)