import os

MENUOPTIONS = ("A", "P", "Q")

def clearScreen ():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def loadBook (filename="phonebook.dat"):
    pbook = dict()
    try:
        fhandler = open(filename, "r")
    except IOError:
        return pbook

    for line in fhandler:
        parts = line.split("|")
        if len(parts) == 3:
            pbook[(parts[0], parts[1])] = parts[2]
    fhandler.close()
    return pbook

def writeBook (pbook, filename="phonebook.dat"):
    try:
        fhandler = open(filename, "w")
    except IOError:
        print "Invalid filename or no permission in folder"
        return
    for key, value in pbook.items():
        entry = key[0]+"|"+key[1]+"|"+value+"\n"
        fhandler.write(entry)
    fhandler.close()

def addEntry (pbook):
    clearScreen()
    lastName = raw_input("Last Name:").replace("|", "-")
    firstName = raw_input("First Name:").replace("|", "-")
    phone = raw_input("Phone Number:").replace("|", "-")

    key = (lastName.title(), firstName.title())
    pbook[key] = phone
    return pbook

def printBook (pbook):
    keyList = pbook.keys()
    clearScreen()

    if len(keyList) == 0:
        print "Empty Phonebook"
    else:
        keyList.sort()
        for lastName, firstName in keyList:
            entry = pbook[(lastName, firstName)]
            print lastName, ",", firstName, ":", entry[:len(entry)-1]

    print ""
    while True:
        if not raw_input("Press <enter> to continue"):
            break

def showMenu ():
    clearScreen()
    print "Choose an action:"
    print "A - add a new entry to the phonebook"
    print "P - print phonebook"
    print "Q - quit phonebook"
    print "====================================="
