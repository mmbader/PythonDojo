factorial = int(raw_input("Enter a number: "))
calculation = 1

for f in range(factorial) :
	if f < 1 :
		continue
	calculation = calculation * f

calculation = calculation * factorial
print str(factorial) + "! =", calculation 
