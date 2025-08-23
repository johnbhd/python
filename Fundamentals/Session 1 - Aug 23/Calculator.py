#Basic calculator ask user 2 number inputs - 8/23/25  4:42pm

operators = ["+",  "-",  "*", "/"]

def Main():
    while True:
        num1 = input("First Number: ")
        if not num1.isdigit():
            print("Enter number only.\n")
            continue
        num1 = int(num1)
        
        num2 = input("Second Number: ")
        if not num2.isdigit():
            print("Enter number only.\n")
            continue
        num2 = int(num2)
            
        op = input("Operator (+, -, *, /): ")[0]
        
        if op not in operators:
            print("Enter only this operator: "+", ".join(operators) +"\n")
            continue
        
        print("\nResult: ", Calculate(num1, num2, op))
        break
    
def Add(num1, num2):
    return num1 + num2

def Subtract(num1, num2):
    return num1 - num2

def Multiply(num1, num2):
    return num1 * num2

def Division(num1, num2):
    return num1 / num2

def Calculate(num1, num2, op):
    match op:
        case "+":
            return Add(num1, num2)
            
        case "-":
            return Subtract(num1, num2)
            
        case "*":
            return Multiply(num1, num2)
            
        case "/":
            return Division(num1, num2)         
            
Main()     