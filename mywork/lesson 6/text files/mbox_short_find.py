fhand = open("mbox-short.txt")
count = 0
for line in fhand :
    if line.find('uct.ac.za') > 0:
        count = count + 1
print "Number of emails from UCT:", count