import random

# Function definition 
def getDiceValue():
    return random.randint(1, 6)

# Executable Code    
dice1 = getDiceValue()
dice2 = getDiceValue()

print "Dice 1:     ", dice1
print "Dice 2:     ", dice2
print "Dice Total: ", dice1 + dice2