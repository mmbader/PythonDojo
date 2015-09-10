from phonebook import phones

phoneBook = phones.loadBook("phonebook.dat")

while True:
    while True:
        phones.showMenu()
        option = raw_input("> ").upper()
        if option in phones.MENUOPTIONS:
            break

    if option == "A":
        phoneBook = phones.addEntry(phoneBook)
        phones.writeBook(phoneBook, "phonebook.dat")
    elif option == "P":
        phones.printBook(phoneBook)
    else:
        quit()
