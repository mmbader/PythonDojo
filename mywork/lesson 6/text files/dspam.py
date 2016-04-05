fhand = open("mbox-short.txt")
count = 0
sum = 0
for line in fhand :
    if line.find('X-DSPAM-Confidence') == 0:
        sum = sum + float(line[line.find(':')+2:])
        count = count + 1
print "The average X-DPSAM-Confidence is", sum/count