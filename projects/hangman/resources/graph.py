__author__ = 'cabarca'

class Graph():
    def __init__(self):
        from os import path
        location = path.dirname(path.abspath(__file__))+"/"
        try:
            fhandler = open(location+"ascii_art.txt")
        except IOError:
            return None

        self.__hangmanArray = list()
        graphStr = None
        for line in fhandler:
            if line.startswith("#"):
                if graphStr is not None:
                    self.__hangmanArray.append(graphStr)
                graphStr = "\n"
            else:
                graphStr += line

    def getHangman(self, guess):
        if guess > len(self.__hangmanArray):
            return None
        return self.__hangmanArray[guess-1]

    @property
    def availableGuesses(self):
        return len(self.__hangmanArray)
