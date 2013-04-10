from turtle import *
'''
setup (width=200, height=200, startx=0, starty=0)

speed ("slow") # important! turtle is intolerably slow otherwise
tracer (False)    # This too: rendering the 'turtle' wastes time

for i in range(200):
    forward(i)
    right(90.5)

done()
'''

'''
Input: Four lists with coordinates, each one is a list of x and y coordinates - W1, W2, A, B - Integers.
Output: Hits the wall or not, True or False
Example:
checkio([[0, 0], [0, 2], [5, 1], [3, 1]]) == True
checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False
checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True
checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False
checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True
checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False
'''

def checkio(data):
    xw1, yw1 = data[0]
    xw2, yw2 = data[1]
    xa, ya = data[2]
    xb, yb = data[3]
    setup (width=200, height=200, startx=0, starty=0)    
    speed ("slow") # important! turtle is intolerably slow otherwise
    tracer (False)    # This too: rendering the 'turtle' wastes time
    forward(60)
    left(90.5)
    done()
    return True





print checkio([[0,0], [0,2], [5,1], [3,1]]) == True, "First"
#print checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "Reverse First"
#print checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "Second"
#print checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "Third"
#print checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "Fourth, shot in butt of wall :)"
#print checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "Fifth, parallel"