try:
    fhandler = open(raw_input("File to create:"), "w")
except IOError:
    print ("Invalid file name or no permissions on directory")
    quit()

while True:
    line = raw_input("> ")
    if not line:
        fhandler.close()
        quit()
    line += "\n"
    fhandler.write(line)
