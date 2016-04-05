fpointer = open(raw_input("Filename: "), "w")
while True:

    line = raw_input("Please enter text or hit enter without typing anything for exit: ")
    
    if line == '':
        break
        
    else:   
        lineFull = line+("\n")
        fpointer.write(lineFull)

fpointer.close()