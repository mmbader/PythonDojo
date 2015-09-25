__author__ = 'cabarca'

class NumberToText:
    
    def __init__(self):
        self.__numbers = dict()
        self.__tenths = dict()
        self.__prefix = dict()

        self.__numbers[1] = "One"
        self.__numbers[2] = "Two"
        self.__numbers[3] = "Three"
        self.__numbers[4] = "Four"
        self.__numbers[5] = "Five"
        self.__numbers[6] = "Six"
        self.__numbers[7] = "Seven"
        self.__numbers[8] = "Eight"
        self.__numbers[9] = "Nine"
        self.__numbers[10] = "Ten"
        self.__numbers[11] = "Eleven"
        self.__numbers[12] = "Twelve"
        self.__numbers[13] = "Thirteen"
        self.__numbers[14] = "Fourteen"
        self.__numbers[15] = "Fifteen"
        self.__numbers[16] = "Sixteen"
        self.__numbers[17] = "Seventeen"
        self.__numbers[18] = "Eighteen"
        self.__numbers[19] = "Nineteen"

        self.__tenths[2] = "Twenty"
        self.__tenths[3] = "Thirty"
        self.__tenths[4] = "Forty"
        self.__tenths[5] = "Fifty"
        self.__tenths[6] = "Sixty"
        self.__tenths[7] = "Seventy"
        self.__tenths[8] = "Eighty"
        self.__tenths[9] = "Ninety"

        self.__prefix[1] = "Thousand"
        self.__prefix[2] = "Million"
        self.__prefix[3] = "Billion"

    def convert(self, number):
        if number == 0:
            return "Cero"
        elif number is None or number < 0 or number > 999999999999:
            raise ValueError

        breakapart = list()
        text = ""

        while number > 0:
            breakapart.append(number % 1000)
            number /= 1000
            if number < 1000:
                breakapart.append(number)
                number = 0

        prefixIdx = len(breakapart) - 1

        for part in list(reversed(breakapart)):
            if part > 0:
                hundred = int(part / 100)
                tenth = part % 100
                if hundred > 0:
                    text += self.__numbers.get(hundred)
                    if tenth > 0:
                        text += " Hundred and "
                    else:
                        text += " Hundred "

                if tenth > 0:
                    if tenth in self.__numbers:
                        text += self.__numbers.get(tenth)
                    else:
                        text += self.__tenths.get(int(tenth/10))+" "+self.__numbers.get(tenth % 10)

                text += " " + self.__prefix.get(prefixIdx, "") + " "

            prefixIdx -= 1

        return text.rstrip()
