try:
    fhandler = open("words.txt", "r")
except IOError:
    print "File 'words.txt' does not exist"
    quit()

for line in fhandler:
    line = line.upper()
    print line[:len(line)-1]  # Avoids extra line break

fhandler.close()
