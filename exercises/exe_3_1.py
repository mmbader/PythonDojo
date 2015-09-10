def computePay(p_hours, p_rate) :
    if (p_hours > 40.0):
        overtime = p_hours - 40
    else:
        overtime = 0
    return p_rate * (1.5 * overtime + 40 )
    
    
try:
    hours = float(raw_input("Input the hours worked: "))
    rate = float(raw_input("Enter the rate per hour: "))
except:
    print "The values entered must be numbers"
else:
    print "Gross Pay: ", computePay(hours, rate)