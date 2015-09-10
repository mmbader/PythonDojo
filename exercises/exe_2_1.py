try:
    hours = float(raw_input("Input the hours worked: "))
    rate = float(raw_input("Enter the rate per hour: "))
except:
    print "The values entered must be numbers"
else:
    if (hours > 40.0):
        overtime = hours - 40
    else:
        overtime = 0
    
    print "Gross Pay: ", rate * (1.5 * overtime + 40 ) 