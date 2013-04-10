import random
'''

class RectangularRoom(object):
    def __init__(self, width, height):
        # store width & height
        # Initialize a whole object usable Dict: {(0,0):False,...,(max,max):Flase}

    def cleanTileAtPosition(self, pos):

        # pos is a Position Object
        # thus, have pos.?x and pos.?y
        # can be checked in Dict as (pos.?x,pos.?x) >>> CAUTION

    def isTileCleaned(self, m, n):
        # Check dict for value

    def getNumTiles(self):
        # something * something  

    def getNumCleanedTiles(self):
        # count for True Values in Dict

    def getRandomPosition(self):
        # Make sure which kind of random method to use 
        # return Position(random number, random number)

    def isPositionInRoom(self, pos):
        # is Position(?x,?y) in {room}

>>> d = {'key':'value'}
>>> print d
{'key': 'value'}
>>> d['mynewkey'] = 'mynewvalue'
'''
# 6.00x Problem Set 7: Simulating robots

import math
import random

import ps7_visualize
import pylab

# For Python 2.7:
from ps7_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, comment out what's above and
# uncomment this line (for Python 2.6):
# from ps7_verify_movement26 import testRobotMovement


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        raise NotImplementedError
    """
        self.width = width
        self.height = height
        d = dict()
        for i in range(width):
            for y in range(height):
                d[(i,y)] = False
        self.d = d

    def showallf(self):
        d = self.d
        return d


    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.pos = pos
        self.d[pos] = True

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        #self.m = m
        #self.n = n
        if self.d[(m,n)] == True:
            return True
        else:
            return False


    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
                """
        return len(self.d)



    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        counter = 0
        for i in range(self.width):
            for y in range(self.height):
                if self.d[(i,y)] == True:
                    counter += 1
        return counter

    def getRandomPosition(self):
        """
        Return a random position inside the room.
        returns: a Position object.
        # Make sure which kind of random method to use 
        # return Position(random number, random number)
        """
        x = random.randrange(self.width)
        y = random.randrange(self.height)
        return Position(x,y)
        #return Position(x,y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if pos.getX() >= self.width and pos.getY() >= self.height:
            return False
        else:
            return True



ffff = Position(5,5)
somer = RectangularRoom(3,3)
somer1 = somer.cleanTileAtPosition((0,1))
#somer1 = somer.cleanTileAtPosition((3,3))
print somer.showallf()

print somer.isTileCleaned(0,1)
print somer.getNumTiles()
print somer.getNumCleanedTiles()
print somer.getRandomPosition()
print somer.isPositionInRoom(ffff)
