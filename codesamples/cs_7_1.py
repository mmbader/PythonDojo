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

for key in wordCount.keys() :
    print key,":",wordCount[key]