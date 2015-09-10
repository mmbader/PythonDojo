gradeSum = 0
gradeCount = 0

while True :
	try :
		grade = float(raw_input("Enter a grade: "))
	except :
		break
	else :
		gradeSum = gradeSum + grade
		gradeCount = gradeCount +1

if gradeCount > 0 :
	print "The grade average is:", gradeSum / gradeCount  
else :
	print  "The grade average is: 0.0"
