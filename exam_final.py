
def m2(l):
    return sum(l)/len(l)

def v2(l):
    mu = m2(l)
    temp = 0
    for e in l:
        temp += (e-mu)**2
    return temp / len(l)

q=[0,1,2,3,4,5,6,7,8]
w=[5,10,10,10,15]
e=[0,1,2,4,6,8]
r=[6,7,11,12,13,15]
t=[9,0,0,3,3,3,6,6]

#print m2(q),m2(w),m2(e),m2(r),m2(t)
#print v2(q),v2(w),v2(e),v2(r),v2(t)

class EdxStudent(object):
      def __init__(self,first,last):
             self.setName("given",first)
             self.setName("family",last)

      def setName(self,which,name):
            if which == "given" or which == "first":
                  self.firstName = name
                  print name
            elif which == "family" or which == "last":
            	  print name
                  self.lastName = name
            else:
                  raise ChoiceError(which)

      def getName(self,which):
            if which == "given" or which == "first":
                  return firstName
            elif which == "family" or which == "last":
                  return lastName
            raise ChoiceError(which)

class ChoiceError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr("Invalid value for name field:"+self.value)


firstName = "Raquel"
lastName = "Pomplun"

try:
        student = EdxStudent(firstName,lastName)

        initialFirstName = student.getName("first")
        initialLastName = student.getName("last")


        newFirstName = student.getName("given")
        newLastName = student.getName("family")

        if initialFirstName == newFirstName and initialLastName == newLastName:
               print "Passed unit test 1"
        else:
               print "Failed unit test 1"

        student.setName("given","LeBron")
        student.setName("family","James")
        print "LeBron"+"James"
        print student.getName("first")+student.getName("last")

        if "LeBron"+"James" == student.getName("first")+student.getName("last"):
               print "Passed unit test 2"
        else:
               print "Failed unit test 2"

except ChoiceError as e:
       print "Failed unit test. Exception is:",
       print e