try:
    fpointer = open(raw_input("Filename: "))
except IOError:
    print "The specified file does not exist!"
    exit()
    