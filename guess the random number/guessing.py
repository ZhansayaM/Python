import random
def guess( ) :
  upperbound = 1000
  secret = random.randrange( upperbound )
  #print( f"secret = {secret}" )
  print( "hello, please guess my secret number" )
  print( f"it lies between 0 and {upperbound-1}\n" )
  attempts = 0
  while 1:
    mess = f"guess {attempts}: "
    inputstring = input( mess )
# Reads input string
    guess = int( inputstring )
# Transforms into int.

    if guess==secret:
      print("Congratulations")
      break;
    else:
      print("You didn't guess the number")
      attempts+=1
      continue