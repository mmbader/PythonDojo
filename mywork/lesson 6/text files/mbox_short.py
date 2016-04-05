fhand = open("mbox-short.txt")
count = 0
for line in fhand :
    if line.startswith('From'):
        print line
    count = count + 1
print "Sender Count:", count