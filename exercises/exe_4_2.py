import random

# Function definition 
def getDiceValue():
    return random.randint(1, 6)

# Executable Code   
point = None

print "First roll of the dice..."

while True :
    if (not raw_input("Ready to start? hit <Enter>")) :
        break
        
diceSum = getDiceValue() + getDiceValue()

print "You Rolled:", diceSum

# Rules of first role
if (diceSum == 2 or diceSum == 3 or diceSum == 12) :
    print "You crapped out!!"
elif (diceSum == 7 or diceSum == 11) :
    print "You win!!"
else :
    point = diceSum
    print "Your point is:", point
    while True:
        while True :
            if (not raw_input("Ready for your next roll? hit <Enter>")) :
                break

        diceSum = getDiceValue() + getDiceValue()
        
        # Rules of following rolls
        print "You Rolled:", diceSum
        if (diceSum == 7) :
            print "Seven out!!"
            break
        elif (diceSum == point) :
            print "You win!!"
            break