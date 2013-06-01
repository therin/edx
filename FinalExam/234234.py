class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
 
def insert(atMe, newFrob):

    if atMe.myName() < newFrob.myName():
        if atMe.getAfter()==None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        else:
            changeFrob = atMe.getAfter()
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
            newFrob.setAfter(changeFrob)
            changeFrob.setBefore(newFrob)
    else:
        if atMe.getBefore()==None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        else:
            changeFrob = atMe.getBefore()
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            newFrob.setBefore(changeFrob)
            changeFrob.setAfter(newFrob)
 


def findFront(start):
    if (start.getBefore()==None):
        return start
    else:
        return findFront(start.getBefore())


eric = Frob('eric')
andrew = Frob('andrew')
aadrew = Frob('aadrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')
 
insert(eric, andrew)
insert(aadrew, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)
insert(eric, Frob('martha'))


print findFront(martha)


