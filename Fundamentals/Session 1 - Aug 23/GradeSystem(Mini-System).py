# simple Grading system - mini system sesssion 1 done - 8/24/25 3:47pm at kfc nagtahan sunday

def Main():
    grades = []
    i = 1
    avg = 0
    
    while True:
        grade = input(f"Enter your Subject {i} grade (type \"stop\" to calculate): ")
        
        if grade.lower() == "stop":
            print("\nGrades: ",grades)
            print("Average: ",GradeCalculate(grades))
            break
        
        try:
            grade = int(grade)
            grades.append(grade)
            i += 1
            GradeCalculate(grades)
            
        except ValueError:
            print("Enter number only or type \"stop\" to calculate grade.  \n")                      

def GradeCalculate(grades):
    avg = sum(grades) / len(grades)
    return avg
    
                                                    
Main()