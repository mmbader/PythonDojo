try:
    fhandler = open("words.txt", "r")
except IOError:
    print "File 'words.txt' does not exist"
    quit()

wordCount = 0
for line in fhandler:
    words = line.split()
    wordCount += len(line)

print "Total words:", wordCount
# not required but a good practice
fhandler.close()
