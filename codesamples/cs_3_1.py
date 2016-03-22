__author__ = 'cabarca'

def addNumbers (num1, num2):
    return num1 + num2

def printTwice (valToPrint):
    print valToPrint
    print valToPrint

x = addNumbers(4, 6)
y = printTwice("hello")

print "The value of x is:", x
print "The value of y is:", y
print "Type of x is: ", type(x)
print "Type of y is: ", type(y)

