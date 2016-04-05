numberList = []

while True:

    print 'Please enter an integer. Enter "done" for exit.'
    line = raw_input('> ')

    if line == 'done':
        break
        
    else:
        try:
            val = int(line)
            numberList.append(val)
        except ValueError:
            print("That's not an integer!")

if numberList == []:
    print 'Done! But your list is empty.'
else:
    print 'Done!'
    print 'Numbers entered', numberList
    print 'Length of list', len(numberList)
    print 'Maximum of list', max(numberList)
    print 'Minimum of list', min(numberList)
    print 'Average of list', float(sum(numberList))/len(numberList)

    numberListSorted = list(numberList)
    numberListSorted.sort()

    print 'Sorted list', numberListSorted

    if len(numberList)%2 == 0:
        middle1 = len(numberList)/2 - 1
        middle2 = middle1 +1 
        print 'The two middle elements are', numberList[middle1], 'and', numberList[middle2]
    else:
        middle = len(numberList)/2
        print 'The middle element is', numberList[middle]