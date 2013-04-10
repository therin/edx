low=0
high=100
guess=(low+high)/2
print 'Please think of a number between 0 and 100!'
print "Is your secret number" + ' ' + str(guess)+'?'
raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess  is to low. Enter 'c' to indicate I guessed correctly.")
if 'h':
  high = guess
elif 'l':
  low = guess
elif 'c':
      print"Game over. Your secret number was:" +'' +'guess'