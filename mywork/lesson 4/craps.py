import random

def throwDice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sumOfDice = dice1+dice2
    print "Dice A shows", dice1
    print "Dice B shows", dice2
    print "The sum of dice A and dice B is", sumOfDice
    return sumOfDice
    
print "First Round:"
gameRound = throwDice()

if gameRound in (7,11): 
    print "You win!"
elif gameRound in (2,3,12):
    print "You lose!"
else:
    point = gameRound
    print "The point", point, "is set"
    while True:
        print ""
        if not raw_input("Hit Enter to continue"):
            print "Next Round:"
            gameRound = throwDice()
            if gameRound == point:
                print "You win!"
                break
            elif gameRound == 7:
                print "You loose!"
                break