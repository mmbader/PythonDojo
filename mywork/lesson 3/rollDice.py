import random

def rollDice():
 x = random.randint(1,6)
 y = random.randint(1,6)
 z = x+y
 print "Dice A shows", x
 print "Dice B shows", y
 print "The sum of dice A and dice B is", z
 
rollDice()
rollDice()
rollDice()