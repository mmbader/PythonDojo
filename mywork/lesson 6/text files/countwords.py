fhand = open("words.txt")
count = 0
for line in fhand :
    words = line.split() #The method split() returns a list of all the words in the string
    for word in words :
        count = count + 1
print "Number of words", count