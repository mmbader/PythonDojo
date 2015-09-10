numberList = list()
while True:
    userInput = raw_input("Enter a number: ")
    if userInput == "done":
        break

    try:
        number = float(userInput)
    except ValueError:
        print "The value entered is not a number"
        continue
    else:
        numberList.append(number)

if len(numberList) == 0:
    print "No numbers were entered"
else:
    print "---"
    # Total numbers entered
    print "Entered numbers: ", len(numberList)
    # sum of numbers
    print "The sum of the entered numbers is:", sum(numberList)
    # maximum and minimum
    print "The maximum number is:", max(numberList)
    print "The minimum number is:", min(numberList)
    # sorted set of numbers
    sortedList = list()
    sortedList.extend(numberList)
    sortedList.sort()
    print "The numbers entered sorted are :"
    for row in sortedList :
        print "  ", row
    # the number in the middle
    listIndex = (len(numberList) / 2) - 1
    if len(numberList)% 2 == 0:
        print "The numbers in the middle of the list are:",numberList[listIndex], "and", numberList[listIndex+1]
    else:
        print "The number in the middle of the list is:", numberList[listIndex]