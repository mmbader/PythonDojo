# Definition of computeGrade function
def computeGrade(p_score) :
    try :
        if ( p_score < 0.0 or p_score > 1.0 ):
            raise ValueError
        elif (p_score >= 0.9):
            letterGrade = "A"
        elif (p_score >= 0.8):
            letterGrade = "B"
        elif (p_score >= 0.7):
            letterGrade = "C"
        elif (p_score >= 0.6):
            letterGrade = "D"
        else:
            letterGrade = "F"
    except ValueError:
        raise ValueError
    else:
        return letterGrade

# Block that executes during call  
try :
    grade = float(raw_input("Enter a grade (0.0 - 1.0): "))
except:
    print "The grade should be a number between 0.0 and 1.0"
else :
    try :
        letter = computeGrade(grade)
    except ValueError:
        print "The value entered is out of range"
    else :
        print "The letter corresponding to the value (", grade, ") is: ", letter