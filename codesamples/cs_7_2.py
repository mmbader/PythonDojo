try :  
    fhandler = open(raw_input("Filename: "))
except :
    print "File not found!"
    exit()

wordCount = dict()

for line in fhandler :
    words = line.split()
    for word in words :
        if word not in wordCount :
            wordCount[word] = 0
        
        wordCount[word] = wordCount[word] + 1
        
orderedList = list()

for key, value in wordCount.items() :
    orderedList.append( (value, key) )

orderedList.sort(reverse=True)
rsetCounter = 1
for count, word in orderedList:
    print word,":",count
    rsetCounter = rsetCounter +1
    if rsetCounter > 5 :
        break