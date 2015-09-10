try :
    grade = float(raw_input("Enter a grade (0.0 - 1.0): "))
except:
    print "The grade should be a number between 0.0 and 1.0"
else :
    try :
        if ( grade < 0.0 or grade > 1.0 ):
            raise ValueError
        elif (grade >= 0.9):
            letterGrade = "A"
        elif (grade >= 0.8):
            letterGrade = "B"
        elif (grade >= 0.7):
            letterGrade = "C"
        elif (grade >= 0.6):
            letterGrade = "D"
        else:
            letterGrade = "F"
    except ValueError:
        print "The value entered is out of range"
    else:
        print "The letter corresponding to the value (", grade, ") is: ", letterGrade
        