numberCount = 0
numberSum = 0
numberMin = None
numberMax = None

while True :
    try :
        inputNum = raw_input("Enter a number (or done to finish): ")
        if (inputNum == "done") :
            break
        else :
            inputNum = float(inputNum)
    except :
        print "Invalid value entered"
        continue
    else :
        numberCount = numberCount +1
        numberSum = numberSum + inputNum
        if (numberMin is None or inputNum < numberMin) :
            numberMin = inputNum
        if (numberMax is None or inputNum > numberMax) :
            numberMax = inputNum

print "Total of Numbers:", numberCount
if (numberCount > 0) :
    print "Maximum Number  :", numberMax
    print "Minimum Number  :", numberMin
    print "Average         :", numberSum / numberCount