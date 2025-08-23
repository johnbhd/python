# age clasifier - 8/23/25  5:07pm

def Main():
    
    while True:
        clasifier = ["Child", "Teen", "Adult", "Senior"]
        
        try:
            age = int(input("Enter age to continue: "))
            print(classifyAge(age, clasifier)+".\n")
            
        except ValueError:
             print("Enter only number.\n")
             
def classifyAge(age, clasifier):
    if  age < 13 and age > 0:
        return clasifier[0]
        
    elif age >= 13 and age <= 19:
        return clasifier[1]
    
    elif age >= 20 and age < 60:
        return clasifier[2]
        
    elif age >= 60:
        return clasifier[3]
        
    else:
        return "Age not accepted." 
        
Main()

