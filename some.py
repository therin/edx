low=0
high=100
print 'Please think of a number between 0 and 1100!'
s = "a"
while s != "c":
  guess=(low+high)/2
  print "Is your secret number" + ' ' + str(guess)+'?'
  s = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess  is to low. Enter 'c' to indicate I guessed correctly.")
  if s == 'h':
    high = guess
  elif s =='l':
    low = guess
  elif s == 'c':
    print "Game over. Your secret number was:" +' ' + str(guess)
  else:
    print "Sorry, I did not understand your input."