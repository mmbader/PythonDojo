__author__ = 'cabarca'

def clearScreen ():
    import os
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
